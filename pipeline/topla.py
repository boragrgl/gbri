"""GBRI Faz 1 - toplama.

Kaynaklari okur, son GERI_GUN gunun yayinlarini aday kayit olarak data/adaylar/ altina yazar.
Ayni belge iki kez yazilmaz. Kaynak durumu data/kaynaklar.json'a, tarama ozeti
data/tarama-gunlugu.json'a eklenir.

Kullanim: python pipeline/topla.py [--geri-gun 92] [--baslangic-arsivi]
"""
import argparse
import datetime as dt
import glob
import json
import os
import sys
import re
import traceback

sys.path.insert(0, os.path.dirname(__file__))
from kaynak_tanimlari import KAYNAKLAR  # noqa: E402
from okuyucular import OKUYUCULAR  # noqa: E402
from ortak import kisa_hash, normal_url, simdi  # noqa: E402

KOK = os.path.join(os.path.dirname(__file__), "..", "data")


def oku_json(yol, varsayilan):
    try:
        with open(yol, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return varsayilan


def yaz_json(yol, veri):
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=1, default=str)
        f.write("\n")


ELEME = [
    ("ecb", re.compile(r"/press/(inter|key)/|/speeches/|/interviews/|/economic-bulletin/|/scpwps/|/blog/", re.I), "url"),
    ("worldbank", re.compile(r"Climate Finance Assessment|Country Climate and Development|Project|DPO\b|"
                             r"Development Effectiveness|Clima|Climat|İklim ve Kalkınma|[^\x00-\u024F\u0130\u0131\u015E\u015F\u011E\u011F]"), "baslik_orijinal"),
]


def elenir(k):
    """Bankacilik duzenlemesiyle ilgisi olmayacagi bastan belli olanlar (konusma, roportaj, proje belgesi)."""
    for kurum, desen, alan in ELEME:
        if k["kurum"] == kurum and desen.search(k.get(alan) or ""):
            return True
    return False


def mevcut_adaylar():
    kayitlar = {}
    for yol in glob.glob(os.path.join(KOK, "adaylar", "*.json")):
        for k in oku_json(yol, []):
            if not elenir(k):
                kayitlar[k["url_normal"]] = k
        os.remove(yol)  # yeniden yazilacak
    return kayitlar


def kaynak_oku(kaynak, baslangic, bugun):
    """Bir kaynagin tum okuyucularini calistirir; (adaylar, hatalar) dondurur."""
    adaylar, hatalar = [], []
    for ok in kaynak["okuyucular"]:
        tip = ok["tip"]
        ayar = {a: b for a, b in ok.items() if a != "tip"}
        ayar.update(kurum=kaynak["id"], baslangic=baslangic, bitis=bugun)
        try:
            for k in OKUYUCULAR[tip](**ayar):
                if k.get("_sayfa_sonu"):
                    if k["en_eski"] and k["en_eski"] < baslangic:
                        break  # sayfalar artik pencereden eski
                    continue
                adaylar.append(k)
        except Exception as e:
            hatalar.append(f"{tip} {ok.get('url', '')}: {type(e).__name__}: {str(e)[:200]}")
            traceback.print_exc()
    return adaylar, hatalar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--geri-gun", type=int, default=int(os.environ.get("GERI_GUN", "92")))
    ap.add_argument("--baslangic-arsivi", action="store_true",
                    help="Bu calistirmada bulunanlar 'yeni' sayilmaz (gecmis veri yuklemesi)")
    ap.add_argument("--kaynak", help="Yalnizca bu kaynak (deneme icin)")
    a = ap.parse_args()

    zaman = simdi()
    bugun = zaman.date()
    baslangic = bugun - dt.timedelta(days=a.geri_gun)
    eski = mevcut_adaylar()
    durumlar = {d["id"]: d for d in oku_json(os.path.join(KOK, "kaynaklar.json"), [])}
    yeni_sayisi, ozet = 0, []

    for kaynak in KAYNAKLAR:
        if a.kaynak and kaynak["id"] != a.kaynak:
            continue
        d = durumlar.get(kaynak["id"], {"id": kaynak["id"], "ardisik_hata": 0})
        d.update(ad=kaynak["ad"], bolge=kaynak["bolge"], aktif=kaynak.get("aktif", True),
                 yontem=sorted({o["tip"] for o in kaynak["okuyucular"]}), not_=kaynak.get("not"))
        d["adresler"] = [o.get("url") for o in kaynak["okuyucular"] if o.get("url")]
        if not d["aktif"] or not kaynak["okuyucular"]:
            durumlar[kaynak["id"]] = d
            ozet.append({"kaynak": kaynak["id"], "durum": "kapali" if not d["aktif"] else "ayri_okuyucu_yok"})
            continue

        adaylar, hatalar = kaynak_oku(kaynak, baslangic, bugun)
        bulunan, eklenen = 0, 0
        for k in adaylar:
            if not k.get("url") or not k.get("baslik_orijinal"):
                continue
            t = k.get("yayin_tarihi")
            if t and (t < baslangic or t > bugun + dt.timedelta(days=1)):
                continue
            if elenir(k):
                continue
            bulunan += 1
            un = normal_url(k["url"])
            if un in eski:
                eski[un]["son_gorulme"] = zaman.isoformat()
                continue
            kurum = k["kurum"]
            if kurum == "ifrs" and re.search(r"issb|sustainab|ifrs-s[12]|climate", k["url"].lower()):
                kurum = "issb"
            eski[un] = {
                "aday_id": f"{kurum}-{t.isoformat() if t else 'tarihsiz'}-{kisa_hash(un)}",
                "kurum": kurum, "url": k["url"], "url_normal": un, "baslik_orijinal": k["baslik_orijinal"],
                "yayin_tarihi": t.isoformat() if t else None, "tarih_kaynagi": k.get("tarih_kaynagi"),
                "kategori": k.get("kategori", ""), "ozet_kaynak": k.get("ozet_kaynak", ""),
                "tespit_zamani": zaman.isoformat(), "son_gorulme": zaman.isoformat(),
                "baslangic_arsivi": bool(a.baslangic_arsivi), "analiz_durumu": "bekliyor",
            }
            eklenen += 1
        yeni_sayisi += eklenen
        d["son_taramada_bulunan"] = bulunan
        if hatalar and not bulunan:
            d["ardisik_hata"] = d.get("ardisik_hata", 0) + 1
            d["son_hata"] = hatalar[0]
        else:
            d["ardisik_hata"] = 0
            d["son_basarili_tarama"] = zaman.isoformat()
            d["son_hata"] = hatalar[0] if hatalar else None
        durumlar[kaynak["id"]] = d
        ozet.append({"kaynak": kaynak["id"], "bulunan": bulunan, "yeni": eklenen, "hata": len(hatalar)})
        print(f"{simdi():%H:%M:%S} {kaynak['id']:12s} bulunan={bulunan:4d} yeni={eklenen:4d} hata={len(hatalar)}", flush=True)

    # aylara gore yaz
    aylar = {}
    for k in eski.values():
        ay = k["yayin_tarihi"][:7] if k["yayin_tarihi"] else "tarihsiz"
        aylar.setdefault(ay, []).append(k)
    for ay, liste in aylar.items():
        liste.sort(key=lambda k: (k["yayin_tarihi"] or "", k["aday_id"]), reverse=True)
        yaz_json(os.path.join(KOK, "adaylar", f"{ay}.json"), liste)
    yaz_json(os.path.join(KOK, "kaynaklar.json"), list(durumlar.values()))
    gunluk = oku_json(os.path.join(KOK, "tarama-gunlugu.json"), [])
    gunluk.insert(0, {"zaman": zaman.isoformat(), "pencere_baslangic": baslangic.isoformat(),
                      "baslangic_arsivi": a.baslangic_arsivi, "yeni": yeni_sayisi, "kaynaklar": ozet})
    yaz_json(os.path.join(KOK, "tarama-gunlugu.json"), gunluk[:30])
    print(f"TOPLAM yeni aday: {yeni_sayisi}")


if __name__ == "__main__":
    main()
