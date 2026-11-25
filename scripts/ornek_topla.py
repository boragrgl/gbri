"""Faz 1 hazirlik: kaynak sayfalarindan ornek indirir (okuyucular bunlara gore yazilir)."""
import html, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from faz0_kaynak_testi import fetch, decode

out = sys.argv[2]
os.makedirs(out, exist_ok=True)
for line in open(sys.argv[1], encoding="utf-8"):
    if not line.strip():
        continue
    name, url = line.split()
    r = fetch(url)
    text = decode(r["body"]) if r["body"] else ""
    open(f"{out}/{name}.html", "w", encoding="utf-8").write(text)
    links = []
    for m in re.finditer(r'<a\b[^>]*href=["\']([^"\'#]+)["\'][^>]*>(.*?)</a>', text, re.S | re.I):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
        links.append(f"{urllib.parse.urljoin(r['final_url'], html.unescape(m.group(1)))}\t{t[:150]}")
    open(f"{out}/{name}.links.tsv", "w", encoding="utf-8").write("\n".join(links))
    print(name, r["status"], len(text), len(links), flush=True)
    time.sleep(2)
