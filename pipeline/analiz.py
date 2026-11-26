"""Faz 2: suzgecten gecen adaylari indirir, Gemini ile iliskilendirir ve analiz eder.
Kullanim: python pipeline/analiz.py [--sinir N] [--kurum k1,k2] [--yeniden] [--ids a,b]"""
import argparse
import datetime as dt
import glob
import gzip
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ortak import simdi, kisa_hash  # noqa: E402
from metin import metin_al, alinti_bul, MAKS_KARAKTER  # noqa: E402
from yz import YZ, Kota  # noqa: E402
from istemler import ILGI_SISTEM, ANALIZ_SISTEM  # noqa: E402

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ONEM = ["Kritik", "Yüksek", "Orta", "Düşük"]
STATU = ["Taslak", "İstişare", "Nihai", "Yürürlükte", "Bilgi amaçlı"]
TUR = ["Kanun", "Yönetmelik", "Tebliğ", "Genelge", "Rehber", "Standart", "İstişare dokümanı", "Rapor",
       "Basın duyurusu", "Bülten", "Konuşma"]
KONU = ["TFRS 9", "Basel", "Sürdürülebilirlik", "Risk Yönetimi", "Diğer"]
DUZEY = ["Yüksek", "Orta", "Düşük", "Dolaylı", "Etki beklenmiyor", "İlgili değil"]
TARIH_DUZELT_KAYNAKLARI = {"url_ay", "belgeden_okunacak", "tahmini"}
BOLUMLER = ["amac", "onceki_cerceve", "teknik_etkiler", "operasyonel_etki", "sermaye_rwa", "iklim"]


def yol(*p):
    return os.path.join(KOK, *p)


def oku(p, varsayilan):
    try:
        return json.load(open(p, encoding="utf-8"))
    except FileNotFoundError:
        return varsayilan


def yaz(p, veri):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(veri, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def tarih_ok(s):
    try:
        return dt.date.fromisoformat(s) if s else None
    except (ValueError, TypeError):
        return None


def sec(deger, liste, varsayilan):
    return deger if deger in liste else varsayilan


def kisalt(metin):
    if len(metin) <= MAKS_KARAKTER:
        return metin, False
    return metin[:MAKS_KARAKTER], True


def bolum_dogrula(b, belge, sayac):
    """Teyitli hukumlerin alintisini belgede dogrular; dogrulanamayani olasi etkiye tasir."""
    if not isinstance(b, dict):
        return {"teyitli": [], "olasi_etki": []}
    teyitli, olasi = [], [str(x) for x in (b.get("olasi_etki") or []) if x]
    for t in b.get("teyitli") or []:
        if not isinstance(t, dict) or not t.get("hukum"):
            continue
        sayac[1] += 1
        alinti = (t.get("alinti") or "").strip()
        ok = False
        if alinti and "..." not in alinti and "…" not in alinti and len(alinti.split()) <= 25:
            ok, sayfa, paragraf = alinti_bul(alinti, belge)
        if ok:
            sayac[0] += 1
            teyitli.append({"hukum": t["hukum"], "alinti": alinti, "sayfa": sayfa, "paragraf": paragraf,
                            "alinti_dogrulandi": True})
        else:
            olasi.append(f"{t['hukum']} (belgeden birebir doğrulanamadı)")
    out = {"teyitli": teyitli, "olasi_etki": olasi}
    if "ilgili_degil" in b:
        out["ilgili_degil"] = bool(b["ilgili_degil"])
    if "karsilastirma_kaynagi" in b:
        out["karsilastirma_kaynagi"] = sec(b["karsilastirma_kaynagi"], ["arsiv", "genel_bilgi"], "genel_bilgi")
    return out


def analizi_temizle(a, belge):
    sayac = [0, 0]
    out = {"yonetici_ozeti": str(a.get("yonetici_ozeti") or "")}
    for k in BOLUMLER:
        out[k] = bolum_dogrula(a.get(k), belge, sayac)
    out["degisiklikler"] = [
        {x: str(d[x]) for x in ("konu", "onceki", "yeni", "referans") if d.get(x)}
        for d in (a.get("degisiklikler") or []) if isinstance(d, dict) and d.get("konu") and d.get("yeni")]
    par = {}
    for p in ("PD", "LGD", "EAD", "ECL"):
        v = (a.get("parametre_etkisi") or {}).get(p) or {}
        par[p] = {"duzey": sec(v.get("duzey"), DUZEY, "İlgili değil"), "not": str(v.get("not") or "")}
    out["parametre_etkisi"] = par
    out["tarihler"] = [{"tur": str(t.get("tur")), "tarih": t.get("tarih") if tarih_ok(t.get("tarih")) else None,
                        **({"referans": str(t["referans"])} if t.get("referans") else {})}
                       for t in (a.get("tarihler") or []) if isinstance(t, dict) and t.get("tur")]
    out["gozden_gecirilecekler"] = [
        {"baslik": str(g["baslik"]), **({"aciklama": str(g["aciklama"])} if g.get("aciklama") else {})}
        for g in (a.get("gozden_gecirilecekler") or []) if isinstance(g, dict) and g.get("baslik")]
    out["referanslar"] = [
        {"metin": str(r["metin"]), "sayfa": r.get("sayfa") if isinstance(r.get("sayfa"), int) else None,
         "paragraf": r.get("paragraf") if isinstance(r.get("paragraf"), int) else None}
        for r in (a.get("referanslar") or []) if isinstance(r, dict) and r.get("metin")]
    return out, sayac


def guven(sayac, kisaltildi, belge):
    dog, top = sayac
    if len(belge["tam"]) < 400:
        return "Düşük"
    oran = dog / top if top else 0
    if kisaltildi or top == 0:
        return "Orta" if oran >= 0.8 else "Düşük"
    return "Yüksek" if oran >= 0.9 else ("Orta" if oran >= 0.6 else "Düşük")


def yeni_id(aday, tarih):
    return f"{aday['kurum']}-{tarih}-{aday['aday_id'].rsplit('-', 1)[-1]}"


def isle(aday, yz, bugun):
    """Tek adayi isler. {'kayit':..., 'durum': ...} doner."""
    belge = metin_al(aday["url"])
    govde, kisaltildi = kisalt(belge["tam"])
    hash_ = kisa_hash(belge["tam"], 16)
    if len(belge["tam"]) < 200:
        return {"durum": "metin_yok", "hash": hash_, "karakter": len(belge["tam"])}
    ust = (f"Kurum: {aday['kurum'].upper()}\nListedeki başlık: {aday['baslik_orijinal']}\n"
           f"Listedeki tarih: {aday.get('yayin_tarihi')}\nAdres: {aday['url']}\n")
    # 1) ilgi kontrolu (kisa metin)
    k, model, _ = yz.json_iste(ILGI_SISTEM, ust + "\nBelge metni (başı):\n" + govde[:7000])
    tarih = aday.get("yayin_tarihi")
    t_model = tarih_ok(k.get("yayin_tarihi"))
    if t_model and not (t_model > bugun) and (bugun - t_model).days < 800:
        if not tarih or aday.get("tarih_kaynagi") in TARIH_DUZELT_KAYNAKLARI:
            tarih = t_model.isoformat()
    if not tarih:
        tarih = bugun.isoformat()
        tarih_kaynak = "tespit"
    else:
        tarih_kaynak = "belge" if (t_model and tarih == t_model.isoformat()) else aday.get("tarih_kaynagi", "liste")
    kayit = {
        "id": yeni_id(aday, tarih), "kurum": aday["kurum"],
        "baslik_orijinal": (k.get("baslik_orijinal") or aday["baslik_orijinal"]).strip(),
        "baslik_tr": (k.get("baslik_tr") or aday["baslik_orijinal"]).strip(),
        "url": aday["url"],
        "belge_turu": sec(k.get("belge_turu"), TUR, "Basın duyurusu"),
        "statu": sec(k.get("statu"), STATU, "Bilgi amaçlı"),
        "onem": "Düşük", "onem_gerekcesi": str(k.get("gerekce") or ""),
        "konu": "Diğer", "ozet_tek_satir": str(k.get("ozet_tek_satir") or ""),
        "yayin_tarihi": tarih, "tarih_kaynagi": tarih_kaynak,
        "tespit_zamani": aday["tespit_zamani"], "baslangic_arsivi": bool(aday.get("baslangic_arsivi")),
        "ilgili_mi": bool(k.get("ilgili_mi")),
        "surumler": [{"no": 1, "tespit_zamani": aday["tespit_zamani"], "icerik_hash": hash_}],
    }
    if not kayit["ilgili_mi"]:
        return {"durum": "ilgisiz", "kayit": kayit, "belge": belge, "hash": hash_}
    # 2) tam analiz
    a, model, kul = yz.json_iste(ANALIZ_SISTEM, ust + "\nBelge metni:\n" + govde)
    analiz, sayac = analizi_temizle(a.get("analiz") or {}, belge)
    kayit.update({
        "onem": sec(a.get("onem"), ONEM, "Orta"), "onem_gerekcesi": str(a.get("onem_gerekcesi") or ""),
        "konu": sec(a.get("konu"), KONU, "Diğer"),
        "alt_konular": [str(x) for x in (a.get("alt_konular") or [])],
        "etkilenen_alanlar": [str(x) for x in (a.get("etkilenen_alanlar") or [])],
        "gorus_son_tarihi": a.get("gorus_son_tarihi") if tarih_ok(a.get("gorus_son_tarihi")) else None,
        "yururluk_tarihi": a.get("yururluk_tarihi") if tarih_ok(a.get("yururluk_tarihi")) else None,
        "uyum_son_tarihi": a.get("uyum_son_tarihi") if tarih_ok(a.get("uyum_son_tarihi")) else None,
        "analiz": analiz,
        "analiz_bilgisi": {"model": model, "olusturma_zamani": simdi().isoformat(),
                           "gonderilen_karakter": len(govde), "alinti_dogrulanan": sayac[0],
                           "alinti_toplam": sayac[1], "guven": guven(sayac, kisaltildi, belge)},
    })
    if kisaltildi:
        kayit["analiz_bilgisi"]["not"] = f"Belge uzun olduğu için ilk {MAKS_KARAKTER} karakter analiz edildi."
    return {"durum": "tamam", "kayit": kayit, "belge": belge, "hash": hash_}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sinir", type=int, default=0, help="en fazla N belge")
    ap.add_argument("--kurum", default="", help="virgulle ayrilmis kurumlar")
    ap.add_argument("--ids", default="", help="virgulle ayrilmis aday_id'ler")
    ap.add_argument("--yeniden", action="store_true", help="tamamlananlari da yeniden isle")
    ap.add_argument("--cesitli", action="store_true", help="--sinir ile kurumlara yayarak sec")
    args = ap.parse_args()
    bugun = simdi().date()
    kurumlar = {x for x in args.kurum.split(",") if x}
    idler = {x for x in args.ids.split(",") if x}

    dosyalar = sorted(glob.glob(yol("data", "adaylar", "*.json")))
    veri = {f: oku(f, []) for f in dosyalar}
    bekleyen = [(f, a) for f, l in veri.items() for a in l
                if a.get("filtre", {}).get("sonuc") == "gecti"
                and (args.yeniden or a.get("analiz_durumu") in (None, "bekliyor", "hata"))
                and (not kurumlar or a["kurum"] in kurumlar) and (not idler or a["aday_id"] in idler)]
    bekleyen.sort(key=lambda x: x[1].get("yayin_tarihi") or "9999", reverse=True)
    if args.sinir and args.cesitli:
        gorulen, secilen = {}, []
        for f, a in bekleyen:
            if gorulen.get(a["kurum"], 0) < 1 and len(secilen) < args.sinir:
                gorulen[a["kurum"]] = 1
                secilen.append((f, a))
        for f, a in bekleyen:
            if len(secilen) >= args.sinir:
                break
            if (f, a) not in secilen:
                secilen.append((f, a))
        bekleyen = secilen
    elif args.sinir:
        bekleyen = bekleyen[:args.sinir]
    print(f"Islenecek belge: {len(bekleyen)}", flush=True)
    yz = YZ()
    ozet = {"tamam": 0, "ilgisiz": 0, "metin_yok": 0, "hata": 0, "kota": 0}
    for n, (f, a) in enumerate(bekleyen, 1):
        print(f"[{n}/{len(bekleyen)}] {a['kurum']} {a.get('yayin_tarihi')} {a['baslik_orijinal'][:70]}", flush=True)
        try:
            s = isle(a, yz, bugun)
        except Kota as e:
            print("  KOTA/MODEL SORUNU, duruyorum:", str(e)[:200], flush=True)
            ozet["kota"] += 1
            break
        except Exception as e:
            print("  HATA:", type(e).__name__, str(e)[:200], flush=True)
            a["analiz_durumu"] = "hata"
            a["analiz_hatasi"] = f"{type(e).__name__}: {str(e)[:200]}"
            ozet["hata"] += 1
            yaz(f, veri[f])
            continue
        a["analiz_durumu"] = s["durum"]
        a.pop("analiz_hatasi", None)
        ozet[s["durum"]] = ozet.get(s["durum"], 0) + 1
        if s["durum"] in ("tamam", "ilgisiz"):
            k = s["kayit"]
            ay = k["yayin_tarihi"][:7]
            p = yol("data", "yayinlar", f"{ay}.json")
            liste = [x for x in oku(p, []) if x["id"] != k["id"]]
            liste.append(k)
            liste.sort(key=lambda x: (x["yayin_tarihi"], x["id"]), reverse=True)
            yaz(p, liste)
            os.makedirs(yol("data", "metin"), exist_ok=True)
            with gzip.open(yol("data", "metin", k["id"] + ".txt.gz"), "wt", encoding="utf-8") as g:
                g.write(s["belge"]["tam"])
            a["kayit_id"] = k["id"]
            print(f"  -> {s['durum']} | {k['onem']} | {k['konu']} | {k['baslik_tr'][:70]}", flush=True)
        yaz(f, veri[f])
    print("OZET", json.dumps(ozet), "| model:", yz.model, "| cagri:", yz.cagri, flush=True)


if __name__ == "__main__":
    main()
