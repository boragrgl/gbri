"""IMF erisim testi: robots.txt'ye uyarak RSS, basin bildirileri, yayin listeleri."""
import sys, json
sys.path.insert(0, ".")
from pipeline.ortak import getir, robots_izin

URLLER = [
 "https://www.imf.org/en/publications/index.json",
 "https://www.imf.org/en/publications/gfsr/index.json",
 "https://www.imf.org/en/publications/fm/index.json",
 "https://www.imf.org/en/blogs/index.json",
 "https://www.imf.org/en/publications/working-papers/index.json",
 "https://www.imf.org/en/publications/wp/issues/index.json",
 "https://www.imf.org/en/publications/staff-discussion-notes/index.json",
 "https://www.imf.org/en/publications/policy-papers/issues/index.json",
 "https://www.imf.org/en/publications/fsap/index.json",
 "https://www.imf.org/en/publications/weo/index.json",
 "https://www.imf.org/en/publications/ger/index.json",
 "https://www.imf.org/en/publications/fandd/index.json",
 "https://www.imf.org/en/news/index.json",
]
import re
sonuc = []
for u in URLLER:
    try:
        if not robots_izin(u):
            sonuc.append({"url": u, "robots": "izin_yok"}); continue
        r = getir(u, deneme=2, zaman_asimi=30)
        m = r["metin"]
        d = {"url": u, "durum": r["durum"], "boyut": len(m)}
        try:
            j = json.loads(m)
            d["anahtarlar"] = list(j.keys())
            it = j.get("items") or []
            d["item_sayisi"] = len(it)
            d["ilk_itemler"] = it[:2]
            d["tarihler"] = [x.get("date") for x in it[:40]]
            d["sections"] = [(x.get("heading"), x.get("content","")[:300]) for x in (j.get("sections") or [])][:6]
        except Exception as e:
            d["json_hata"] = str(e)[:100]
        sonuc.append(d)
    except Exception as e:
        sonuc.append({"url": u, "hata": str(e)[:200]})
    print(json.dumps(sonuc[-1], ensure_ascii=False)[:3000], flush=True)
json.dump(sonuc, open("reports/imf-testi.json", "w"), ensure_ascii=False, indent=1)
