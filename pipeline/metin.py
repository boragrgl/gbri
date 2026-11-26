"""Belge metni cikarma: HTML ve PDF -> sayfa/paragraf numarali duz metin."""
import html
import re
import subprocess
import tempfile
import os

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


def _pdf_sayfalari(ham):
    with tempfile.TemporaryDirectory() as d:
        yol = os.path.join(d, "x.pdf")
        open(yol, "wb").write(ham)
        try:
            out = subprocess.run(["pdftotext", "-layout", yol, "-"], capture_output=True, timeout=120).stdout
            metin = out.decode("utf-8", "replace")
        except Exception:
            metin = ""
        if len(metin.strip()) < 50:
            try:
                from pypdf import PdfReader
                r = PdfReader(yol)
                return [(p.extract_text() or "") for p in r.pages]
            except Exception:
                return []
    return metin.split("\f")


def metin_al(url):
    """{'tur','sayfalar'(liste[str]),'paragraflar'(liste[str]) ,'tam'} doner."""
    r = getir(url)
    ham = r["ham"]
    if ham[:4] == b"%PDF" or "pdf" in r["tur"].lower() or url.lower().endswith(".pdf"):
        sayfalar = [re.sub(r"[ \t]+", " ", p).strip() for p in _pdf_sayfalari(ham)]
        sayfalar = [p for p in sayfalar if p] or []
        tam = "\n".join(f"[Sayfa {i}]\n{p}" for i, p in enumerate(sayfalar, 1))
        return {"tur": "pdf", "sayfalar": sayfalar, "paragraflar": [], "tam": tam, "ham_uzunluk": len(ham)}
    paragraflar = _html_metin(r["metin"])
    tam = "\n".join(f"[P{i}] {p}" for i, p in enumerate(paragraflar, 1))
    return {"tur": "html", "sayfalar": [], "paragraflar": paragraflar, "tam": tam, "ham_uzunluk": len(ham)}


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
    if belge["tur"] == "pdf":
        for i, p in enumerate(belge["sayfalar"], 1):
            if a in _anahtar(p):
                return True, i, None
        # sayfa sinirini asan alinti
        if a in _anahtar(" ".join(belge["sayfalar"])):
            return True, None, None
        return False, None, None
    for i, p in enumerate(belge["paragraflar"], 1):
        if a in _anahtar(p):
            return True, None, i
    if a in _anahtar(" ".join(belge["paragraflar"])):
        return True, None, None
    return False, None, None
