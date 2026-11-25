"""GBRI toplama hatti - ortak yardimcilar (yalnizca standart kutuphane)."""
import datetime as dt
import gzip
import hashlib
import html
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

USER_AGENT = "GBRI-regulatory-monitor/0.2 (daily check of official publications; github.com/boragrgl/gbri)"
TR = dt.timezone(dt.timedelta(hours=3))
_robots = {}


def simdi():
    return dt.datetime.now(TR).replace(microsecond=0)


def robots_izin(url):
    p = urllib.parse.urlparse(url)
    kok = f"{p.scheme}://{p.netloc}"
    if kok not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            r = getir(kok + "/robots.txt", robots_kontrol=False, deneme=1)
            rp.parse(r["metin"].splitlines()) if r["durum"] == 200 else None
            _robots[kok] = rp if r["durum"] == 200 else None
        except Exception:
            _robots[kok] = None
    rp = _robots[kok]
    return True if rp is None else rp.can_fetch(USER_AGENT, url)


def _coz(body):
    if body[:2] == b"\x1f\x8b":
        body = gzip.decompress(body)
    for enc in ("utf-8", "windows-1254", "iso-8859-9"):
        try:
            return body.decode(enc)
        except UnicodeDecodeError:
            continue
    return body.decode("utf-8", "replace")


def getir(url, robots_kontrol=True, deneme=3, zaman_asimi=40, bekle=1.5):
    """Sayfayi indirir. {'durum','url','tur','metin','ham'} doner; hata durumunda istisna atar."""
    if robots_kontrol and not robots_izin(url):
        raise PermissionError(f"robots.txt izin vermiyor: {url}")
    son_hata = None
    for i in range(deneme):
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT, "Accept-Encoding": "gzip",
            "Accept": "text/html,application/xhtml+xml,application/xml,application/rss+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8"})
        try:
            with urllib.request.urlopen(req, timeout=zaman_asimi) as r:
                ham = r.read(20_000_000)
                time.sleep(bekle)
                return {"durum": r.status, "url": r.geturl(), "tur": r.headers.get("Content-Type", ""),
                        "metin": _coz(ham) if "pdf" not in r.headers.get("Content-Type", "") else "", "ham": ham}
        except urllib.error.HTTPError as e:
            son_hata = e
            if e.code in (403, 404, 410):
                break
        except Exception as e:  # zaman asimi, baglanti
            son_hata = e
        time.sleep(3 * (i + 1))
    raise son_hata


def temiz(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def kisa_hash(s, n=6):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:n]


def normal_url(url):
    p = urllib.parse.urlsplit(url.strip())
    path = re.sub(r"/{2,}", "/", p.path)
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower(), path, p.query, ""))


# ---- tarih okuma -------------------------------------------------------
AYLAR = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3, "apr": 4, "april": 4, "may": 5,
    "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8, "august": 8, "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10, "nov": 11, "november": 11, "dec": 12, "december": 12,
    "oca": 1, "ocak": 1, "şub": 2, "şubat": 2, "sub": 2, "subat": 2, "mart": 3, "nis": 4, "nisan": 4,
    "mayıs": 5, "mayis": 5, "haz": 6, "haziran": 6, "tem": 7, "temmuz": 7, "ağu": 8, "ağustos": 8, "agu": 8,
    "agustos": 8, "eyl": 9, "eylül": 9, "eylul": 9, "eki": 10, "ekim": 10, "kas": 11, "kasım": 11, "kasim": 11,
    "ara": 12, "aralık": 12, "aralik": 12,
}
_AY = "|".join(sorted(AYLAR, key=len, reverse=True))
TARIH_DESENLERI = [
    (re.compile(r"\b(\d{4})-(\d{2})-(\d{2})"), lambda m: (int(m[1]), int(m[2]), int(m[3]))),
    (re.compile(r"\b(\d{1,2})[./](\d{1,2})[./](\d{4})\b"), lambda m: (int(m[3]), int(m[2]), int(m[1]))),
    (re.compile(r"\b(\d{1,2})\s+(" + _AY + r")\.?,?\s+(\d{4})\b", re.I), lambda m: (int(m[3]), AYLAR[m[2].lower()], int(m[1]))),
    (re.compile(r"\b(" + _AY + r")\.?\s+(\d{1,2}),?\s+(\d{4})\b", re.I), lambda m: (int(m[3]), AYLAR[m[1].lower()], int(m[2]))),
]


def tarih_bul(metin):
    """Metindeki tarihleri (konum, date) listesi olarak dondurur."""
    out = []
    for desen, f in TARIH_DESENLERI:
        for m in desen.finditer(metin):
            try:
                y, a, g = f(m)
                if 1990 <= y <= 2100:
                    out.append((m.start(), dt.date(y, a, g)))
            except (ValueError, KeyError):
                continue
    return sorted(out)


def rss_tarih(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(s).date()
    except Exception:
        pass
    t = tarih_bul(s)
    return t[0][1] if t else None
