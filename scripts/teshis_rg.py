import sys, os
sys.path.insert(0, "pipeline")
from ortak import getir
from metin import _pdf_sayfalari
URLS = ["https://www.resmigazete.gov.tr/eskiler/2026/11/20261118-6.pdf",
        "https://www.resmigazete.gov.tr/eskiler/2026/11/20261111-5.pdf",
        "https://www.resmigazete.gov.tr/eskiler/2026/11/20261106-3.pdf"]
for u in URLS:
    for v in (u, u[:-4] + ".htm", u[:-4] + ".html"):
        try:
            r = getir(v)
            ham = r["ham"]
            n = 0
            if ham[:4] == b"%PDF":
                n = sum(len(p) for p in _pdf_sayfalari(ham))
            print(v[-28:], r["durum"], r["tur"], len(ham), "pdf_metin=", n, ham[:80].replace(b"\n", b" "), flush=True)
            if r["metin"]:
                print("   metin:", r["metin"][:300].replace("\n", " "), flush=True)
        except Exception as e:
            print(v[-28:], "HATA", type(e).__name__, str(e)[:120], flush=True)
