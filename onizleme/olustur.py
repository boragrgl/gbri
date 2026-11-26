"""data/ altindaki gercek verilerden tek dosyalik onizleme sayfasi uretir."""
import json,glob,os
k=os.path.dirname(os.path.abspath(__file__))+"/.."
tum=[x for f in sorted(glob.glob(k+"/data/yayinlar/*.json")) for x in json.load(open(f,encoding="utf-8"))]
il=[x for x in tum if x.get("ilgili_mi") and x.get("analiz")]
KONU={"TFRS 9":"TFRS 9","Basel":"Basel","Sürdürülebilirlik":"Sürdürülebilirlik","Risk Yönetimi":"Risk Yönetimi"}
veri={"bugun":"2026-11-26","yayinlar":il,"ilgisiz":len(tum)-len(il),
      "kaynaklar":[{"ad":s["ad"],"aktif":s["aktif"],"ardisik_hata":s["ardisik_hata"]} for s in json.load(open(k+"/data/kaynaklar.json",encoding="utf-8"))]}
s=open(k+"/onizleme/sablon.html",encoding="utf-8").read()
j=json.dumps(veri,ensure_ascii=False).replace("</","<\\/")
open(k+"/onizleme/index.html","w",encoding="utf-8").write(s.replace("__VERI__",j))
print(len(il),"kayit,",os.path.getsize(k+"/onizleme/index.html"),"bayt")
