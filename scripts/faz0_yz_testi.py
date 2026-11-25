"""GBRI Faz 0 - yapay zeka testi (GitHub Models).

Gercek 3 kaynak metnini GitHub Models'e gonderir, Turkce yapilandirilmis
analiz ister ve sonucu raporlar. Ayrica "teyitli" denen alintilarin kaynak
metinde birebir gecip gecmedigini kontrol eder.

Kimlik: GitHub Actions icindeki GITHUB_TOKEN (is akisinda models: read izni).
Kullanim: python scripts/faz0_yz_testi.py reports/
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
from faz0_kaynak_testi import decode, fetch  # noqa: E402

API = "https://models.github.ai/inference/chat/completions"
CATALOG = "https://models.github.ai/catalog/models"
PREFERRED = ["openai/gpt-4.1", "openai/gpt-4o", "openai/gpt-4.1-mini", "openai/gpt-4o-mini"]
MAX_CHARS = 9000  # ucretsiz katmanin istek basina token sinirina sigmak icin

PROFILE = ("Kamu (devlet) bankasi; kredi riski icin Basel standart yaklasimini kullanir, IRD kullanmaz; "
           "TFRS 9 uygular. Onem duzeyini bu profile gore belirle: bu bankayi dogrudan baglamayan "
           "konular (or. yalnizca IRD bankalarini ilgilendiren hukumler) dusuk onemlidir.")

SYSTEM = f"""Sen bankacilik duzenlemeleri analistisin. Yalnizca verilen belge metnine dayan.
Banka profili: {PROFILE}
Kurallar:
- Belgede olmayan bir yukumluluk uydurma.
- "teyitli" listesine yalnizca belgede acikca yazan hukumleri koy ve her biri icin belgeden BIREBIR kopyalanmis kisa bir alinti ver (en fazla 25 kelime, belgenin orijinal dilinde).
- Kendi yorumlarini yalnizca "olasi_etki" listesine yaz.
- Tum aciklamalar Turkce olsun.
Yalnizca su JSON'u dondur:
{{"ilgili_mi": true/false, "konu": "TFRS 9|Basel|Surdurulebilirlik|Risk Yonetimi|Diger",
 "statu": "Taslak|Istisare|Nihai|Yururlukte|Bilgi amacli",
 "onem": "Kritik|Yuksek|Orta|Dusuk", "onem_gerekcesi": "...",
 "yonetici_ozeti": "3-4 cumle",
 "teyitli": [{{"hukum": "Turkce ozet", "alinti": "belgeden birebir"}}],
 "olasi_etki": ["..."], "tarihler": [{{"tur": "...", "tarih": "YYYY-AA-GG ya da belirtilmemis"}}],
 "etkilenen_alanlar": ["PD","LGD","EAD","ECL","RWA","Likidite","Raporlama", "..."]}}"""


def first_feed_item(url):
    res = fetch(url)
    root = ET.fromstring(res["body"])
    local = lambda el: el.tag.rsplit("}", 1)[-1]
    for el in root.iter():
        if local(el) in ("item", "entry"):
            link = ""
            for c in el:
                if local(c) == "link":
                    link = (c.text or c.get("href") or "").strip()
            title = next(((c.text or "").strip() for c in el if local(c) == "title"), "")
            return title, link
    return "", ""


def page_text(url):
    res = fetch(url)
    text = decode(res["body"]) if res["body"] else ""
    text = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>",
                  " ", text, flags=re.S | re.I)
    import html as h
    return re.sub(r"\s+", " ", h.unescape(re.sub(r"<[^>]+>", " ", text))).strip()


def call(model, doc_title, doc_text, token):
    body = json.dumps({"model": model, "temperature": 0.1, "response_format": {"type": "json_object"},
                       "messages": [{"role": "system", "content": SYSTEM},
                                    {"role": "user", "content": f"Belge basligi: {doc_title}\n\nBelge metni:\n{doc_text}"}]
                       }).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            out = json.loads(r.read())
        return {"ok": True, "elapsed": round(time.time() - t0, 1), "usage": out.get("usage"),
                "content": out["choices"][0]["message"]["content"]}
    except urllib.error.HTTPError as e:
        return {"ok": False, "elapsed": round(time.time() - t0, 1), "error": f"HTTP {e.code}: {e.read()[:400].decode('utf-8', 'replace')}"}
    except Exception as e:
        return {"ok": False, "elapsed": round(time.time() - t0, 1), "error": f"{type(e).__name__}: {e}"[:400]}


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def main(out_dir):
    token = os.environ["GITHUB_TOKEN"]
    # mevcut modeller
    cat = fetch(CATALOG)
    try:
        ids = [m.get("id") for m in json.loads(cat["body"])]
    except Exception:
        ids = []
    models = [m for m in PREFERRED if m in ids] or PREFERRED[:2]

    docs = []
    t, link = first_feed_item("https://www.bis.org/doclist/all_pressrels.rss")
    docs.append(("BIS/BCBS", t, link, page_text(link) if link else ""))
    t, link = first_feed_item("https://www.ecb.europa.eu/rss/pub.html")
    docs.append(("ECB", t, link, page_text(link) if link else ""))
    docs.append(("Resmi Gazete", "Resmi Gazete - gunun icindekiler", "https://www.resmigazete.gov.tr/",
                 page_text("https://www.resmigazete.gov.tr/")))

    results = []
    for model in models[:2]:
        for src, title, link, text in docs:
            r = call(model, title, text[:MAX_CHARS], token)
            r.update({"model": model, "source": src, "title": title, "link": link, "chars_sent": min(len(text), MAX_CHARS)})
            if r["ok"]:
                try:
                    parsed = json.loads(r["content"])
                    quotes = [q.get("alinti", "") for q in parsed.get("teyitli", [])]
                    r["quotes_total"] = len(quotes)
                    r["quotes_verbatim"] = sum(1 for q in quotes if q and norm(q) in norm(text))
                    r["parsed"] = parsed
                except ValueError:
                    r["parsed"] = None
            results.append(r)
            print(model, src, r["ok"], r.get("error", ""), flush=True)
            time.sleep(5)

    json.dump({"catalog_has": [m for m in PREFERRED if m in ids], "catalog_size": len(ids), "results": results},
              open(f"{out_dir}/faz0-yz-testi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    L = ["# Faz 0 · Yapay zekâ testi (GitHub Models)", "",
         f"Katalogdaki model sayısı: {len(ids)} · Denenenler: {', '.join(models[:2])}", "",
         "| Model | Kaynak | Sonuç | Süre (sn) | Gönderilen kr | Token (girdi/çıktı) | Teyitli alıntı birebir | Önem | Statü |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        p = r.get("parsed") or {}
        u = r.get("usage") or {}
        L.append(f"| {r['model']} | {r['source']} | {'OK' if r['ok'] else 'HATA'} | {r['elapsed']} | {r['chars_sent']} | "
                 f"{u.get('prompt_tokens', '-')}/{u.get('completion_tokens', '-')} | "
                 f"{r.get('quotes_verbatim', '-')}/{r.get('quotes_total', '-')} | {p.get('onem', '-')} | {p.get('statu', '-')} |")
    for r in results:
        L += ["", f"## {r['model']} · {r['source']}", f"Belge: {r['title']} — {r['link']}", ""]
        L.append("```json\n" + (json.dumps(r.get("parsed"), ensure_ascii=False, indent=2) if r.get("parsed") else r.get("error", r.get("content", ""))) + "\n```")
    open(f"{out_dir}/faz0-yz-testi.md", "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
