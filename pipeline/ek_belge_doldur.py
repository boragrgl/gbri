"""Mevcut analiz kayitlarina, analizde kullanilan ekli PDF adresini (ek_belge_url) ekler."""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from ortak import getir
from metin import _ana_pdf

KOK = os.path.join(os.path.dirname(__file__), "..", "data", "yayinlar")
toplam = 0
for f in sorted(glob.glob(KOK + "/*.json")):
    d = json.load(open(f, encoding="utf-8")); ch = False
    for x in d:
        if x.get("ek_belge_url") or not x.get("url", "").startswith("http") or x["url"].lower().endswith(".pdf"):
            continue
        if not x.get("ilgili_mi") or not x.get("analiz"):
            continue
        try:
            r = getir(x["url"])
            u = _ana_pdf(r["metin"], r["url"])
        except Exception as e:
            print("HATA", x["id"], str(e)[:80]); continue
        if u:
            x["ek_belge_url"] = u; ch = True; toplam += 1
            print("ek:", x["id"], u[:100])
    if ch:
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("TOPLAM", toplam)
