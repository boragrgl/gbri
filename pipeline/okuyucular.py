"""Kaynak okuyuculari. Her okuyucu aday kayit sozlukleri uretir:
{"kurum","url","baslik_orijinal","yayin_tarihi"(date|None),"ozet_kaynak","kategori","tarih_kaynagi"}
"""
import datetime as dt
import json
import re
import urllib.parse
import xml.etree.ElementTree as ET

from ortak import getir, rss_tarih, tarih_bul, temiz

_A = re.compile(r'<a\b([^>]*)>(.*?)</a>', re.S | re.I)
_HREF = re.compile(r'href\s*=\s*["\']([^"\']+)["\']', re.I)
_BAS_TARIH = re.compile(r"^\s*(\d{1,2}[./]\d{1,2}[./]\d{4}|\d{1,2}\s+\w+\.?\s+\d{4})\s*")
_GENEL = re.compile(r"^(\.*\s*)?(download( document)?|read more|devam[ıi]|detay|indir|pdf)\.*$", re.I)
_BASLIK_ETIKETI = re.compile(r'<h[1-6][^>]*>(.*?)</h[1-6]>', re.S | re.I)


def _yerel(el):
    return el.tag.rsplit("}", 1)[-1]


def rss_ayristir(metin):
    kok = ET.fromstring(metin.encode("utf-8"))
    out = []
    for el in kok.iter():
        if _yerel(el) not in ("item", "entry"):
            continue
        d = {}
        for c in el:
            ad = _yerel(c)
            deger = (c.text or "").strip() or c.get("href", "")
            if ad == "link" and d.get("link"):
                continue
            d.setdefault(ad, deger)
        out.append({"url": d.get("link", ""), "baslik_orijinal": temiz(d.get("title", "")),
                    "yayin_tarihi": rss_tarih(d.get("pubDate") or d.get("date") or d.get("published") or d.get("updated")),
                    "ozet_kaynak": temiz(d.get("description") or d.get("summary") or "")[:600]})
    return out


def rss(kurum, url, sayfa_param=None, max_sayfa=1, kategori="", **_):
    """RSS/Atom; sayfa_param verilirse (or. 'paged') sayfalar sirayla okunur."""
    for s in range(1, max_sayfa + 1):
        u = url if s == 1 or not sayfa_param else f"{url}{'&' if '?' in url else '?'}{sayfa_param}={s}"
        try:
            kayitlar = rss_ayristir(getir(u)["metin"])
        except Exception as e:
            if s == 1:
                raise
            break
        if not kayitlar:
            break
        for k in kayitlar:
            k.update(kurum=kurum, kategori=kategori, tarih_kaynagi="rss")
            yield k


def _en_yakin_tarih(html_metin, bas, son, geri=1500, ileri=700):
    """Baglantinin hemen cevresindeki en yakin tarihi bulur."""
    once = tarih_bul(html_metin[max(0, bas - geri):bas])
    sonra = tarih_bul(html_metin[son:son + ileri])
    adaylar = [(geri - p if bas >= geri else bas - p, d) for p, d in once] + [(p, d) for p, d in sonra]
    return min(adaylar)[1] if adaylar else None


def liste(kurum, url, href_desen, sayfa_sablonu=None, max_sayfa=1, kategori="", tarih_once=1500,
          tarih_sonra=700, baslik_icinde_tarih=False, tarihsiz_kabul=False, **_):
    """HTML liste sayfasi: href deseni tutan baglantilari ve yanindaki tarihi okur."""
    desen = re.compile(href_desen)
    for s in range(max_sayfa):
        u = url if s == 0 or not sayfa_sablonu else url + sayfa_sablonu.format(s=s)
        r = getir(u)
        metin = r["metin"]
        goruldu = {}
        for m in _A.finditer(metin):
            hm = _HREF.search(m.group(1))
            if not hm:
                continue
            href = urllib.parse.urljoin(r["url"], hm.group(1).strip())
            if not desen.search(href):
                continue
            ic = m.group(2)
            hb = _BASLIK_ETIKETI.search(ic)
            baslik = temiz(hb.group(1) if hb else ic)
            if not baslik:
                tm = re.search(r'title\s*=\s*["\']([^"\']+)["\']', m.group(1))
                baslik = temiz(tm.group(1)) if tm else ""
            ic_tarih = tarih_bul(temiz(ic))
            if baslik_icinde_tarih:
                t = tarih_bul(baslik)
                tarih = t[0][1] if t else None
            elif ic_tarih:
                tarih = ic_tarih[0][1]  # baglantinin kendi metnindeki tarih en guvenilir olandir
            else:
                tarih = _en_yakin_tarih(metin, m.start(), m.end(), tarih_once, tarih_sonra)
            baslik = _BAS_TARIH.sub("", baslik).strip()
            baslik = re.sub(r"^(Yeni|Publication|Media release)\s+", "", baslik).strip()
            if _GENEL.match(baslik):
                baslik = ""
            onceki = goruldu.get(href)
            if onceki and len(onceki["baslik_orijinal"]) >= len(baslik):
                continue
            goruldu[href] = {"kurum": kurum, "url": href, "baslik_orijinal": baslik[:400], "yayin_tarihi": tarih,
                             "ozet_kaynak": "", "kategori": kategori, "tarih_kaynagi": "liste"}
        kayitlar = [k for k in goruldu.values() if k["baslik_orijinal"] and (k["yayin_tarihi"] or tarihsiz_kabul)]
        yield from kayitlar
        if not kayitlar:
            break
        yield {"_sayfa_sonu": True, "en_eski": min((k["yayin_tarihi"] for k in kayitlar if k["yayin_tarihi"]), default=None)}


def resmi_gazete(kurum, baslangic, bitis, anahtar_kelimeler, **_):
    """Resmi Gazete gunluk icindekiler; yalnizca anahtar kelime iceren maddeler."""
    kelime = re.compile("|".join(anahtar_kelimeler), re.I)
    g = bitis
    while g >= baslangic:
        u = f"https://www.resmigazete.gov.tr/eskiler/{g:%Y}/{g:%m}/{g:%Y%m%d}.htm"
        try:
            r = getir(u, deneme=2)
        except Exception:
            g -= dt.timedelta(days=1)
            continue
        for m in _A.finditer(r["metin"]):
            hm = _HREF.search(m.group(1))
            if not hm:
                continue
            href = urllib.parse.urljoin(r["url"], hm.group(1).strip())
            if not re.search(rf"/eskiler/{g:%Y}/{g:%m}/{g:%Y%m%d}-\d+\.(htm|pdf)$", href):
                continue
            baslik = temiz(m.group(2)).lstrip("–- ").strip()
            if baslik and kelime.search(baslik):
                yield {"kurum": kurum, "url": href, "baslik_orijinal": baslik, "yayin_tarihi": g, "ozet_kaynak": "",
                       "kategori": "Resmî Gazete", "tarih_kaynagi": "gazete_gunu"}
        g -= dt.timedelta(days=1)


def bddk_mevzuat(kurum, listeler, referans_listeler, baslangic, **_):
    """BDDK mevzuat listeleri. DokumanGetir kimlikleri artan sirada verildigi icin, tarihi yazmayan
    belgelerin tarihi, tarihli kurul kararlarindan kimlik araligiyla tahmin edilir."""
    tarihli = []
    for lid in referans_listeler:
        for k in liste(kurum, f"https://www.bddk.org.tr/Mevzuat/Liste/{lid}", r"/Mevzuat/DokumanGetir/\d+",
                       baslik_icinde_tarih=True, kategori=f"mevzuat-{lid}"):
            if k.get("_sayfa_sonu") or not k["yayin_tarihi"]:
                continue
            k["_id"] = int(k["url"].rsplit("/", 1)[1])
            tarihli.append(k)
            if k["yayin_tarihi"] >= baslangic:
                k["tarih_kaynagi"] = "baslik"
                yield {a: b for a, b in k.items() if a != "_id"}
    tarihli.sort(key=lambda k: k["_id"])

    def tahmin(i):
        if not tarihli:
            return None
        alt = [k for k in tarihli if k["_id"] <= i]
        return (alt[-1] if alt else tarihli[0])["yayin_tarihi"]

    for lid in listeler:
        for k in liste(kurum, f"https://www.bddk.org.tr/Mevzuat/Liste/{lid}", r"/Mevzuat/DokumanGetir/\d+",
                       baslik_icinde_tarih=True, tarihsiz_kabul=True, kategori=f"mevzuat-{lid}"):
            if k.get("_sayfa_sonu"):
                continue
            if not k["yayin_tarihi"]:
                k["yayin_tarihi"] = tahmin(int(k["url"].rsplit("/", 1)[1]))
                k["tarih_kaynagi"] = "tahmini"
            if k["yayin_tarihi"] and k["yayin_tarihi"] >= baslangic:
                yield k


def tarihsiz_pdf_listesi(kurum, url, href_desen, kategori="", **_):
    """Tarih yazmayan duyuru listesi (KGK ana sayfa). Tarih Faz 2'de belgeden okunur."""
    for k in liste(kurum, url, href_desen, tarihsiz_kabul=True, kategori=kategori, tarih_once=0, tarih_sonra=0):
        if not k.get("_sayfa_sonu"):
            k["tarih_kaynagi"] = "belgeden_okunacak"
            yield k


WB_DISLA = re.compile(r"ISR|ESRS|Procurement|Notice|Agreement|Project Information|Environmental|Resettlement|"
                      r"Implementation Status|Disclosable|Official Documents|Loan|Letter|Minutes|Stakeholder|"
                      r"Integrated Safeguards|Appraisal|Restructuring|Audit|Grant|Credit Number|Financing", re.I)


def dunya_bankasi(kurum, sorgular, baslangic, satir=25, **_):
    for q in sorgular:
        u = (f"https://search.worldbank.org/api/v3/wds?format=json&rows={satir}&os=0&fl=docdt,display_title,pdfurl,url,docty"
             f"&qterm={urllib.parse.quote(q)}&strdate={baslangic:%Y-%m-%d}&sort=docdt&order=desc")
        veri = json.loads(getir(u)["metin"])
        for d in (veri.get("documents") or {}).values():
            if not isinstance(d, dict) or "display_title" not in d:
                continue
            if WB_DISLA.search(d["display_title"]) or WB_DISLA.search(d.get("docty", "")):
                continue
            tarih = rss_tarih(d.get("docdt", ""))
            yield {"kurum": kurum, "url": d.get("url") or d.get("pdfurl", ""), "baslik_orijinal": temiz(d["display_title"]),
                   "yayin_tarihi": tarih, "ozet_kaynak": d.get("docty", ""), "kategori": q, "tarih_kaynagi": "api"}


def imf_koleksiyon(kurum, adresler, baslangic, **_):
    """IMF'in resmi, makine-okunur koleksiyon dosyalari (index.json; robots.txt'ye uyar)."""
    for u, kat in adresler:
        try:
            j = json.loads(getir(u)["metin"])
        except Exception:
            continue
        for it in j.get("items") or []:
            try:
                t = dt.datetime.strptime(it.get("date", ""), "%B %d, %Y").date()
            except ValueError:
                continue
            if t < baslangic:
                continue
            yield {"kurum": kurum, "url": it.get("url", ""), "baslik_orijinal": temiz(it.get("title", "")),
                   "yayin_tarihi": t, "ozet_kaynak": temiz(re.sub(r"<[^>]+>", " ", it.get("description", ""))),
                   "kategori": kat, "tarih_kaynagi": "koleksiyon"}


def rss_kesif(kurum, url, kategori="", **_):
    """Adres dogrudan besleme degilse sayfadaki besleme baglantilarini dener (TCMB, IFRS)."""
    r = getir(url)
    m = r["metin"].lstrip()
    if m.startswith("<?xml") or "<rss" in m[:300] or "<feed" in m[:300]:
        for k in rss_ayristir(r["metin"]):
            k.update(kurum=kurum, kategori=kategori, tarih_kaynagi="rss")
            yield k
        return
    adaylar = []
    for am in _A.finditer(r["metin"]):
        hm = _HREF.search(am.group(1))
        if hm and re.search(r"rss|\.xml|feed", hm.group(1), re.I):
            adaylar.append(urllib.parse.urljoin(r["url"], hm.group(1)))
    for a in dict.fromkeys(adaylar):
        try:
            r2 = getir(a, deneme=1)
            if r2["metin"].lstrip().startswith("<?xml") or "<rss" in r2["metin"][:300]:
                for k in rss_ayristir(r2["metin"]):
                    k.update(kurum=kurum, kategori=kategori or a, tarih_kaynagi="rss")
                    yield k
        except Exception:
            continue


def site_haritasi(kurum, url, href_desen, baslangic, kategori="", **_):
    """Site haritasindaki /YYYY/MM/ iceren adresler (IFRS). Tarih ay basina gore; Faz 2'de sayfadan netlesir."""
    desen = re.compile(href_desen)
    metin = getir(url)["metin"]
    for loc in re.findall(r"<loc>([^<]+)</loc>", metin):
        m = desen.search(loc)
        if not m:
            continue
        try:
            t = dt.date(int(m.group("y")), int(m.group("m")), 1)
        except ValueError:
            continue
        if t < baslangic.replace(day=1):
            continue
        slug = loc.rstrip("/").rsplit("/", 1)[-1]
        baslik = re.sub(r"-+", " ", slug).strip().capitalize()
        yield {"kurum": kurum, "url": loc, "baslik_orijinal": baslik, "yayin_tarihi": max(t, baslangic),
               "ozet_kaynak": "", "kategori": kategori, "tarih_kaynagi": "url_ay"}


OKUYUCULAR = {"imf_koleksiyon": imf_koleksiyon, "site_haritasi": site_haritasi, "rss": rss, "liste": liste, "resmi_gazete": resmi_gazete, "bddk_mevzuat": bddk_mevzuat,
              "tarihsiz_pdf_listesi": tarihsiz_pdf_listesi, "dunya_bankasi": dunya_bankasi, "rss_kesif": rss_kesif}
