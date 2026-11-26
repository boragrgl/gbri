"""Belge metni cikarma: HTML ve PDF -> sayfa/paragraf numarali duz metin."""
import html
import re
import subprocess
import tempfile
import os
import urllib.parse

from ortak import getir

MAKS_KARAKTER = 150_000  # modele gonderilen ust sinir


def _html_metin(s):
    s = re.sub(r"(?is)<(script|style|nav|header|footer|noscript|form|svg|aside)\b.*?</\1>", " ", s)
    m = re.search(r"(?is)<(main|article)\b.*?</\1>", s)
    if m and len(m.group(0)) > 1500:
        s = m.group(0)
    s = re.sub(r"(?i)</(p|div|li|h[1-6]|tr|br|section|ul|ol|table)\s*>|<br\s*/?>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    satirlar = [re.sub(r"[ \t ]+", " ", x).strip() for x in s.splitlines()]
    return [x for x in satirlar if len(x) > 2]


def _harf(sayfalar):
    return sum(sum(c.isalpha() for c in p) for p in sayfalar)


def _pdf_sayfalari(ham):
    with tempfile.TemporaryDirectory() as d:
        yol = os.path.join(d, "x.pdf")
        open(yol, "wb").write(ham)
        try:
            out = subprocess.run(["pdftotext", yol, "-"], capture_output=True, timeout=120).stdout
            sayfalar = out.decode("utf-8", "replace").split("\f")
        except Exception:
            sayfalar = []
        if _harf(sayfalar) < 300:
            try:
                from pypdf import PdfReader
                t = [(p.extract_text() or "") for p in PdfReader(yol).pages]
                if _harf(t) > _harf(sayfalar):
                    sayfalar = t
            except Exception:
                pass
        if _harf(sayfalar) < 300:  # tarama ya da bozuk yazi tipi: OCR dene
            o = _ocr(yol, d)
            if _harf(o) > _harf(sayfalar):
                global SON_OCR
                SON_OCR = True
                return o
        return sayfalar


def _ocr(yol, d, maks_sayfa=40):
    """Taranmis PDF: pdftoppm + tesseract (Turkce). Kurulu degilse bos doner."""
    try:
        subprocess.run(["pdftoppm", "-r", "200", "-l", str(maks_sayfa), "-png", yol, os.path.join(d, "s")],
                       capture_output=True, timeout=300, check=True)
        sayfalar = []
        for g in sorted(x for x in os.listdir(d) if x.startswith("s") and x.endswith(".png")):
            r = subprocess.run(["tesseract", os.path.join(d, g), "-", "-l", "tur+eng", "--psm", "4"],
                               capture_output=True, timeout=180)
            sayfalar.append(r.stdout.decode("utf-8", "replace"))
        return sayfalar
    except Exception:
        return []


SON_OCR = False


def _ana_pdf(ham_html, taban):
    """Sayfadaki ilk anlamli PDF baglantisi (yayinin asil metni sik sik burada)."""
    for m in re.finditer(r'(?i)href=["\']([^"\']+\.pdf[^"\']*)["\']', ham_html):
        u = urllib.parse.urljoin(taban, html.unescape(m.group(1)))
        if re.search(r"(?i)privacy|cookie|terms|accessib|factsheet-template", u):
            continue
        return u
    return None


def metin_al(url):
    """{'tur','sayfalar'(liste[str]),'paragraflar'(liste[str]) ,'tam'} doner."""
    b = _metin_al(url)
    if len(b["tam"]) < 400 and "resmigazete.gov.tr" in url and url.lower().endswith(".pdf"):
        try:  # taranmis PDF: ayni maddenin HTML surumu
            b2 = _metin_al(url[:-4] + ".htm", ek_pdf=False)
            if len(b2["tam"]) > len(b["tam"]):
                return b2
        except Exception:
            pass
    return b


def _metin_al(url, ek_pdf=True):
    r = getir(url)
    ham = r["ham"]
    if ham[:4] == b"%PDF" or "pdf" in r["tur"].lower() or url.lower().endswith(".pdf"):
        global SON_OCR
        SON_OCR = False
        sayfalar = [re.sub(r"[ \t]+", " ", p).strip() for p in _pdf_sayfalari(ham)]
        ocr = SON_OCR
        sayfalar = [p for p in sayfalar if p] or []
        tam = "\n".join(f"[Sayfa {i}]\n{p}" for i, p in enumerate(sayfalar, 1))
        return {"tur": "pdf", "sayfalar": sayfalar, "paragraflar": [], "tam": tam, "ham_uzunluk": len(ham), "ocr": ocr}
    paragraflar = _html_metin(r["metin"])
    tam = "\n".join(f"[P{i}] {p}" for i, p in enumerate(paragraflar, 1))
    out = {"tur": "html", "sayfalar": [], "paragraflar": paragraflar, "tam": tam, "ham_uzunluk": len(ham)}
    if ek_pdf:
        pdf_url = _ana_pdf(r["metin"], r["url"])
        if pdf_url:
            try:
                rp = getir(pdf_url)
                sayfalar = [re.sub(r"[ \t]+", " ", p).strip() for p in _pdf_sayfalari(rp["ham"])]
                sayfalar = [p for p in sayfalar if p]
                if sayfalar:
                    out["sayfalar"] = sayfalar
                    out["ek_pdf"] = pdf_url
                    out["tur"] = "karma"
                    out["tam"] = (tam + "\n\n[EK BELGE: sayfadaki PDF bağlantısı]\n"
                                  + "\n".join(f"[Sayfa {i}]\n{p}" for i, p in enumerate(sayfalar, 1)))
            except Exception:
                pass
    return out


def _anahtar(s):
    s = s.replace("­", "").replace("-\n", "")
    s = s.replace("İ", "i").replace("I", "ı").lower()
    return re.sub(r"[\W_]+", "", s)


def alinti_bul(alinti, belge):
    """Alinti belgede birebir var mi? (bosluk/noktalama/buyuk-kucuk harf farklarindan bagimsiz).
    Doner: (bulundu, sayfa|None, paragraf|None)."""
    a = _anahtar(alinti)
    if len(alinti.split()) < 3 or len(a) < 12:
        return False, None, None
    for i, p in enumerate(belge["sayfalar"], 1):
        if a in _anahtar(p):
            return True, i, None
    for i, p in enumerate(belge["paragraflar"], 1):
        if a in _anahtar(p):
            return True, None, i
    if a in _anahtar(" ".join(belge["sayfalar"])) or a in _anahtar(" ".join(belge["paragraflar"])):
        return True, None, None
    return False, None, None
