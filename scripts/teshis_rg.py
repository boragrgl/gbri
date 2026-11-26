import sys
sys.path.insert(0, "pipeline")
import metin
for u in ["https://www.resmigazete.gov.tr/eskiler/2026/11/20261118-6.pdf",
          "https://www.resmigazete.gov.tr/eskiler/2026/11/20261111-5.pdf",
          "https://www.resmigazete.gov.tr/eskiler/2026/11/20261106-3.pdf"]:
    try:
        b = metin.metin_al(u)
        print("SONUC", u[-16:], b["tur"], len(b["tam"]), "ocr=", b.get("ocr"), "sayfa=", len(b["sayfalar"]), repr(b["tam"][:300]), flush=True)
    except Exception as e:
        import traceback; traceback.print_exc()
