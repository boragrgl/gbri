"""IMF erisim testi: robots.txt'ye uyarak RSS, basin bildirileri, yayin listeleri."""
import sys, json
sys.path.insert(0, ".")
from pipeline.ortak import getir, robots_izin

URLLER = [
 "https://www.imf.org/en/publications/wp/index.json",
 "https://www.imf.org/en/publications/policy-papers/index.json",
 "https://www.imf.org/en/publications/sdn/index.json",
 "https://www.imf.org/en/publications/gfsr/index.json",
 "https://www.imf.org/en/publications/fsap/index.json",
 "https://www.imf.org/en/publications/cr/index.json",
 "https://www.imf.org/en/publications/dp/index.json",
 "https://www.imf.org/en/publications/fm/index.json",
 "https://www.imf.org/en/publications/index.json",
 "https://www.imf.org/en/news/articles/index.json",
 "https://www.imf.org/en/news/pressreleases/index.json",
 "https://www.imf.org/en/news/press-releases/index.json",
 "https://www.imf.org/en/blogs/index.json",
 "https://www.imf.org/en/topics/financial-sector/index.json",
]
sonuc = []
for u in URLLER:
    try:
        if not robots_izin(u):
            sonuc.append({"url": u, "robots": "izin_yok"})
        else:
            r = getir(u, deneme=2, zaman_asimi=30)
            m = r["metin"]
            sonuc.append({"url": u, "robots": "izinli", "durum": r["durum"], "tur": r.get("tur"), "boyut": len(m), "ilk": m[:400], "item_sayisi": m.count(chr(34)+"position"+chr(34)).replace("\n", " ")})
    except Exception as e:
        sonuc.append({"url": u, "hata": str(e)[:200]})
    print(sonuc[-1], flush=True)
import re
try:
    m = getir("https://www.imf.org/en/News", deneme=2)["metin"]
    print("LINKS", sorted(set(re.findall(r'href="([^"]*(?:rss|RSS|feed|Feed)[^"]*)"', m)))[:30], flush=True)
    print("ALL", sorted(set(re.findall(r'href="(/en/[^"#?]{3,60})"', m)))[:60], flush=True)
except Exception as e: print("LINKHATA", e)
json.dump(sonuc, open("reports/imf-testi.json", "w"), ensure_ascii=False, indent=1)
