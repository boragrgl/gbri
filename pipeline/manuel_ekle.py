"""Elle eklenen belgeleri (data/manuel/<kurum>/belgeler.json + .md/.pdf metin dosyalari) aday olarak kaydeder.
Kullanim: python pipeline/manuel_ekle.py imf"""
import json, os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(__file__))
from ortak import kisa_hash

KOK = os.path.join(os.path.dirname(__file__), "..", "data")
KURUM_SAYFA = {"imf": "https://www.imf.org/en/publications"}


def main(kurum):
    liste = json.load(open(os.path.join(KOK, "manuel", kurum, "belgeler.json"), encoding="utf-8"))
    yol = {}
    for f in os.listdir(os.path.join(KOK, "adaylar")):
        if f.endswith(".json"):
            yol[f] = json.load(open(os.path.join(KOK, "adaylar", f), encoding="utf-8"))
    var = {a["url_normal"] for l in yol.values() for a in l}
    simdi = dt.datetime.now(dt.timezone(dt.timedelta(hours=3))).isoformat()
    eklenen = 0
    for b in liste:
        un = "dosya:" + b["dosya"]
        if un in var:
            continue
        t = b.get("tarih")
        aday = {"aday_id": f"{kurum}-{t or 'tarihsiz'}-{kisa_hash(un)}", "kurum": kurum, "url": un, "url_normal": un,
                "kaynak_baglantisi": KURUM_SAYFA.get(kurum, ""), "baslik_orijinal": b["baslik"], "yayin_tarihi": t,
                "tarih_kaynagi": b.get("tarih_kaynagi"), "kategori": "Manuel arşiv",
                "ozet_kaynak": "", "tespit_zamani": simdi, "son_gorulme": simdi, "baslangic_arsivi": True,
                "analiz_durumu": "bekliyor",
                "filtre": {"sonuc": "gecti", "neden": "manuel arşiv (kullanıcı ekledi)", "konular": ["Genel düzenleme"]}}
        ay = t[:7] if t else "tarihsiz"
        yol.setdefault(ay + ".json", []).append(aday)
        eklenen += 1
    for f, l in yol.items():
        json.dump(l, open(os.path.join(KOK, "adaylar", f), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("eklenen:", eklenen)


if __name__ == "__main__":
    main(sys.argv[1])
