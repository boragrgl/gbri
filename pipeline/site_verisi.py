"""Site icin veri paketi uretir: site/public/data/{yayinlar,adaylar,kaynaklar}.json"""
import json, glob, os
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def oku(y): return json.load(open(os.path.join(K, y), encoding="utf-8"))
yay = [x for f in sorted(glob.glob(K + "/data/yayinlar/*.json")) for x in json.load(open(f, encoding="utf-8"))]
analizli = [x for x in yay if x.get("ilgili_mi") and x.get("analiz")]
yid = {x["id"] for x in yay}; yurl = {x["url"] for x in yay}
ilgisiz = {x["id"] for x in yay if not (x.get("ilgili_mi") and x.get("analiz"))}
adaylar = []
for f in sorted(glob.glob(K + "/data/adaylar/*.json")):
    for a in json.load(open(f, encoding="utf-8")):
        i = a.get("aday_id") or a.get("kayit_id")
        if i in yid: d = "ilgisiz" if i in ilgisiz else "analiz"
        elif a.get("url") in yurl: d = "analiz"
        else: d = "elendi" if (a.get("filtre") or {}).get("sonuc") == "elendi" else "bekliyor"
        adaylar.append({"id": i, "kurum": a["kurum"], "baslik": a.get("baslik_orijinal"), "url": a["url"],
                        "tarih": a.get("yayin_tarihi"), "durum": d, "neden": (a.get("filtre") or {}).get("neden")})
kay = [{"id": s["id"], "ad": s["ad"], "bolge": s.get("bolge"), "aktif": s["aktif"], "ardisik_hata": s["ardisik_hata"],
        "son_tarama": s.get("son_basarili_tarama")} for s in oku("data/kaynaklar.json")]
cikti = os.path.join(K, "site/public/data"); os.makedirs(cikti, exist_ok=True)
for ad, v in (("yayinlar", analizli), ("adaylar", adaylar), ("kaynaklar", kay)):
    json.dump(v, open(f"{cikti}/{ad}.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(analizli), "yayin,", len(adaylar), "aday,", len(kay), "kaynak")
