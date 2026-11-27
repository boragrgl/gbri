"""IMF erisim testi: robots.txt'ye uyarak RSS, basin bildirileri, yayin listeleri."""
import sys, json
sys.path.insert(0, ".")
from pipeline.ortak import getir, robots_izin

URLLER = [
 "https://www.imf.org/en/rss-list",
 "https://www.imf.org/en/News/RSS?type=Press%20Release",
 "https://www.imf.org/en/Publications/RSS?series=IMF%20Working%20Papers",
 "https://www.imf.org/en/Publications/RSS?series=Global%20Financial%20Stability%20Notes",
 "https://www.imf.org/en/News",
 "https://www.imf.org/en/Publications/Search",
 "https://www.imf.org/sitemap.xml",
]
sonuc = []
for u in URLLER:
    try:
        if not robots_izin(u):
            sonuc.append({"url": u, "robots": "izin_yok"})
        else:
            r = getir(u, deneme=2, zaman_asimi=30)
            m = r["metin"]
            sonuc.append({"url": u, "robots": "izinli", "durum": r["durum"], "tur": r.get("tur"), "boyut": len(m), "ilk": m[:200].replace("\n", " ")})
    except Exception as e:
        sonuc.append({"url": u, "hata": str(e)[:200]})
    print(sonuc[-1], flush=True)
json.dump(sonuc, open("reports/imf-testi.json", "w"), ensure_ascii=False, indent=1)
