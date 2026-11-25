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
MAX_CHARS = 9000  # GitHub Models ucretsiz katmani icin
GEMINI_MAX_CHARS = 40000
GEMINI_API = "https://generativelanguage.googleapis.com/v1beta"

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
            raw = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                import gzip
                raw = gzip.decompress(raw)
            try:
                out = json.loads(raw)
            except ValueError:
                return {"ok": False, "elapsed": round(time.time() - t0, 1),
                        "error": f"JSON degil: HTTP {r.status} {r.headers.get('Content-Type')} url={r.geturl()} govde={raw[:300]!r}"}
        return {"ok": True, "elapsed": round(time.time() - t0, 1), "usage": out.get("usage"),
                "content": out["choices"][0]["message"]["content"]}
    except urllib.error.HTTPError as e:
        return {"ok": False, "elapsed": round(time.time() - t0, 1), "error": f"HTTP {e.code}: {e.read()[:400].decode('utf-8', 'replace')}"}
    except Exception as e:
        return {"ok": False, "elapsed": round(time.time() - t0, 1), "error": f"{type(e).__name__}: {e}"[:400]}


def gemini_pick_model(key):
    req = urllib.request.Request(f"{GEMINI_API}/models?pageSize=200", headers={"x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=60) as r:
        models = json.loads(r.read()).get("models", [])
    names = [m["name"].split("/", 1)[1] for m in models
             if "generateContent" in m.get("supportedGenerationMethods", [])]
    pref = ["gemini-flash-latest", "gemini-2.5-flash", "gemini-3-flash-preview",
            "gemini-3.1-flash-lite", "gemini-flash-lite-latest", "gemini-2.5-flash-lite"]
    pick = [n for n in pref if n in names]
    return pick, names


def call_gemini(model, doc_title, doc_text, key):
    body = json.dumps({
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        "contents": [{"role": "user", "parts": [{"text": f"Belge basligi: {doc_title}\n\nBelge metni:\n{doc_text}"}]}],
        "generationConfig": {"temperature": 0.1, "responseMimeType": "application/json"}}).encode()
    req = urllib.request.Request(f"{GEMINI_API}/models/{model}:generateContent", data=body,
                                 headers={"x-goog-api-key": key, "Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            out = json.loads(r.read())
        um = out.get("usageMetadata", {})
        text = "".join(p.get("text", "") for p in out["candidates"][0]["content"]["parts"])
        return {"ok": True, "elapsed": round(time.time() - t0, 1),
                "usage": {"prompt_tokens": um.get("promptTokenCount"), "completion_tokens": um.get("candidatesTokenCount")},
                "content": text}
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
    print("katalog:", cat["status"], cat["content_type"], cat["body"][:200], flush=True)
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

    plan = [("github", m, MAX_CHARS) for m in models[:1]] if os.environ.get("RUN_GITHUB") else []
    gkey = os.environ.get("GEMINI_API_KEY", "")
    gem_all = []
    if gkey:
        try:
            gpick, gem_all = gemini_pick_model(gkey)
            # ucretsiz katmanda calisan ilk modeli bul
            for m in gpick:
                probe = call_gemini(m, "deneme", "Bu bir baglanti denemesidir. ilgili_mi false olsun.", gkey)
                print("gemini deneme", m, probe["ok"], probe.get("error", "")[:160].replace("\n", " "), flush=True)
                if probe["ok"]:
                    plan.append(("gemini", m, GEMINI_MAX_CHARS))
                    break
                time.sleep(4)
        except Exception as e:
            print("gemini model listesi alinamadi:", type(e).__name__, str(e)[:200], flush=True)
    print("plan:", plan, "| gemini modelleri:", gem_all[:40], flush=True)

    results = []
    for provider, model, limit in plan:
        for src, title, link, text in docs:
            r = (call_gemini(model, title, text[:limit], gkey) if provider == "gemini"
                 else call(model, title, text[:limit], token))
            r.update({"model": f"{provider}:{model}", "source": src, "title": title, "link": link,
                      "chars_sent": min(len(text), limit)})
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
            print(r["model"], src, r["ok"], r.get("error", "")[:300], flush=True)
            time.sleep(6)

    json.dump({"catalog_has": [m for m in PREFERRED if m in ids], "catalog_size": len(ids), "results": results},
              open(f"{out_dir}/faz0-yz-testi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    L = ["# Faz 0 · Yapay zekâ testi (GitHub Models ve Gemini)", "",
         f"Denenenler: {', '.join(p[0] + ':' + p[1] for p in plan)}", "",
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
