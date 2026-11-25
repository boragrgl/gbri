"""GBRI Faz 0 - kaynak erisim testi.

Her kaynagin aday adreslerini GitHub Actions sunucusundan bir kez ister ve
sonuclari raporlar. Sadece Python standart kutuphanesini kullanir.

Ne olculur:
  - robots.txt bu adrese izin veriyor mu
  - HTTP durumu, yonlendirme, icerik turu, boyut, sure
  - Engelleme belirtisi (403/429, captcha, bot korumasi sayfasi)
  - Sayfa basligi, gorunur metin miktari (JS ile mi olusuyor?)
  - PDF baglanti sayisi, RSS/Atom beslemesi var mi, beslemede kac kayit var

Kullanim: python scripts/faz0_kaynak_testi.py config/sources.json reports/
"""
import datetime as dt
import gzip
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET

USER_AGENT = "GBRI-regulatory-monitor/0.1 (daily check of official publications; github.com/boragrgl/gbri)"
TIMEOUT = 30
BLOCK_HINTS = ["captcha", "cf-challenge", "challenge-platform", "access denied", "request rejected",
               "erisim engellendi", "erişim engellendi", "bot detection", "incapsula", "akamai"]


def fill_date(url):
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
    return (url.replace("{YYYY}", f"{today.year:04d}").replace("{MM}", f"{today.month:02d}")
               .replace("{DD}", f"{today.day:02d}"))


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml,application/rss+xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip",
    })
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(5_000_000)
            if r.headers.get("Content-Encoding") == "gzip":
                body = gzip.decompress(body)
            return {"status": r.status, "final_url": r.geturl(), "content_type": r.headers.get("Content-Type", ""),
                    "body": body, "elapsed": round(time.time() - t0, 2), "error": None}
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read(200_000)
        except Exception:
            pass
        return {"status": e.code, "final_url": url, "content_type": e.headers.get("Content-Type", "") if e.headers else "",
                "body": body, "elapsed": round(time.time() - t0, 2), "error": f"HTTP {e.code}"}
    except Exception as e:  # zaman asimi, DNS, TLS, baglanti reddi
        return {"status": None, "final_url": url, "content_type": "", "body": b"",
                "elapsed": round(time.time() - t0, 2), "error": f"{type(e).__name__}: {e}"[:200]}


def robots_allowed(url, cache):
    p = urllib.parse.urlparse(url)
    root = f"{p.scheme}://{p.netloc}"
    if root not in cache:
        rp = urllib.robotparser.RobotFileParser()
        res = fetch(root + "/robots.txt")
        if res["status"] == 200:
            rp.parse(res["body"].decode("utf-8", "replace").splitlines())
            cache[root] = rp
        else:
            cache[root] = None  # robots.txt yok ya da okunamadi -> kisit yok sayilir
    rp = cache[root]
    return True if rp is None else rp.can_fetch(USER_AGENT, url)


def decode(body):
    for enc in ("utf-8", "windows-1254", "iso-8859-9"):
        try:
            return body.decode(enc)
        except UnicodeDecodeError:
            continue
    return body.decode("utf-8", "replace")


def analyse_feed(text):
    try:
        root = ET.fromstring(text.encode("utf-8"))
    except ET.ParseError:
        return None
    local = lambda el: el.tag.rsplit("}", 1)[-1]
    items = [el for el in root.iter() if local(el) in ("item", "entry")]

    def child(el, *names):
        for c in el:
            if local(c) in names and (c.text or "").strip():
                return c.text.strip()
        return ""
    out = [{"title": child(it, "title")[:120], "date": child(it, "pubDate", "updated", "date", "published")}
           for it in items[:3]]
    return {"items": len(items), "latest": out}


def analyse_html(text, base):
    title = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
    stripped = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S | re.I)
    visible = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", stripped))).strip()
    hrefs = re.findall(r'href=["\']([^"\'#]+)["\']', text, re.I)
    pdfs = {h for h in hrefs if ".pdf" in h.lower()}
    feeds = re.findall(r'<link[^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]*>', text, re.I)
    feed_urls = []
    for h in hrefs:
        hl = h.lower()
        if hl.endswith(".rss") or hl.endswith(".xml") or "/rss/" in hl or hl.endswith("/feed/"):
            feed_urls.append(urllib.parse.urljoin(base, html.unescape(h)))
    for f in feeds:
        m = re.search(r'href=["\']([^"\']+)["\']', f, re.I)
        if m:
            feed_urls.append(urllib.parse.urljoin(base, html.unescape(m.group(1))))
    frames = re.findall(r'<i?frame[^>]+src=["\']([^"\']+)["\']', text, re.I)
    return {"frames": [urllib.parse.urljoin(base, f) for f in frames[:3]],
            "title": html.unescape(title.group(1)).strip()[:150] if title else "",
            "visible_chars": len(visible), "links": len(hrefs), "pdf_links": len(pdfs),
            "feed_links": list(dict.fromkeys(feed_urls))[:8]}


def check(url, robots_cache):
    url = fill_date(url)
    allowed = robots_allowed(url, robots_cache)
    res = fetch(url)
    text = decode(res["body"]) if res["body"] else ""
    low = text[:50_000].lower()
    blocked_hint = [h for h in BLOCK_HINTS if h in low]
    row = {"url": url, "robots_allowed": allowed, "status": res["status"], "final_url": res["final_url"],
           "content_type": res["content_type"].split(";")[0], "bytes": len(res["body"]),
           "elapsed_s": res["elapsed"], "error": res["error"], "block_hints": blocked_hint}
    looks_feed = "xml" in row["content_type"] or text.lstrip().startswith("<?xml") or "<rss" in low[:500]
    if text and "json" in row["content_type"]:
        try:
            j = json.loads(text)
            row["json"] = {"keys": list(j.keys())[:10] if isinstance(j, dict) else f"list[{len(j)}]"}
        except ValueError:
            row["json"] = {"keys": "parse_error"}
    elif text and looks_feed:
        row["feed"] = analyse_feed(text)
    elif text:
        row["html"] = analyse_html(text, res["final_url"])
    row["verdict"] = verdict(row)
    return row


def verdict(row):
    if row["error"] and row["status"] is None:
        return "ERISILEMEDI"
    if row["status"] in (401, 403, 429, 503) or row["block_hints"]:
        return "ENGEL_SUPHESI"
    if row["status"] and row["status"] >= 400:
        return "HATA"
    if not row["robots_allowed"]:
        return "ROBOTS_IZIN_YOK"
    if row.get("json"):
        return "JSON_OK" if row["json"]["keys"] != "parse_error" else "HATA"
    if row.get("feed"):
        return "BESLEME_OK" if row["feed"]["items"] else "BESLEME_BOS"
    h = row.get("html") or {}
    if h.get("visible_chars", 0) < 800:
        return "JS_GEREKEBILIR"
    return "OK"


def main(cfg_path, out_dir, name="faz0-kaynak-testi"):
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    robots_cache, results = {}, []
    for src in cfg["sources"]:
        rows = []
        for url in src["candidates"]:
            rows.append(check(url, robots_cache))
            time.sleep(2)  # kurum sitelerine yuk bindirmemek icin
        # sayfada bulunan beslemeleri de bir kez dene
        seen = {r["url"] for r in rows}
        for r in list(rows):
            for f in (r.get("html") or {}).get("feed_links", [])[:src.get("max_discovered", 2)]:
                if f not in seen:
                    seen.add(f)
                    fr = check(f, robots_cache)
                    fr["discovered"] = True
                    rows.append(fr)
                    time.sleep(2)
        results.append({"id": src["id"], "name": src["name"], "region": src["region"], "checks": rows})
        print(src["id"], [r["verdict"] for r in rows], flush=True)

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    json.dump({"run_at": stamp, "results": results}, open(f"{out_dir}/{name}.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    lines = [f"# Faz 0 · Kaynak erişim testi ({name})", "", f"Çalıştırma: {stamp} · GitHub Actions sunucusu", "",
             "| Kaynak | Adres | Sonuç | HTTP | Süre (sn) | Not |", "|---|---|---|---|---|---|"]
    for s in results:
        for r in s["checks"]:
            note = []
            if r.get("feed"):
                note.append(f"besleme: {r['feed']['items']} kayıt")
                if r["feed"]["latest"]:
                    note.append("son: " + r["feed"]["latest"][0]["title"][:60].replace("|", "/"))
            if r.get("json"):
                note.append(f"JSON: {r['json']['keys']}")
            if r.get("html"):
                h = r["html"]
                note.append(f"metin {h['visible_chars']} kr, {h['pdf_links']} PDF")
                if h.get("frames"):
                    note.append("çerçeve: " + ", ".join(h["frames"]))
                if h["feed_links"]:
                    note.append(f"besleme bağlantısı: {len(h['feed_links'])}")
            if r["error"]:
                note.append(r["error"][:80])
            if r["block_hints"]:
                note.append("engel ipucu: " + ",".join(r["block_hints"]))
            if r.get("discovered"):
                note.append("sayfadan bulundu")
            lines.append(f"| {s['id']} | {r['url']} | {r['verdict']} | {r['status']} | {r['elapsed_s']} | {'; '.join(note)} |")
    open(f"{out_dir}/{name}.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], *sys.argv[3:4])
