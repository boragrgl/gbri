import sys, os, subprocess, tempfile
sys.path.insert(0, "pipeline")
from ortak import getir
u = "https://www.resmigazete.gov.tr/eskiler/2026/11/20261118-6.pdf"
ham = getir(u)["ham"]
d = tempfile.mkdtemp()
yol = os.path.join(d, "x.pdf")
open(yol, "wb").write(ham)
for cmd in (["pdfinfo", yol], ["pdftotext", "-layout", yol, "-"], ["pdfimages", "-list", yol],
            ["pdftoppm", "-r", "150", "-l", "2", "-png", yol, os.path.join(d, "s")], ["ls", "-la", d], ["which", "tesseract"]):
    r = subprocess.run(cmd, capture_output=True, timeout=200)
    print("$", " ".join(cmd[:2]), "->", r.returncode, r.stdout[:600].decode("utf-8", "replace"), r.stderr[:400].decode("utf-8", "replace"), flush=True)
png = [x for x in os.listdir(d) if x.endswith(".png")]
if png:
    r = subprocess.run(["tesseract", os.path.join(d, sorted(png)[0]), "-", "-l", "tur+eng", "--psm", "4"], capture_output=True, timeout=200)
    print("tesseract", r.returncode, r.stdout[:800].decode("utf-8", "replace"), r.stderr[:300].decode("utf-8", "replace"))
