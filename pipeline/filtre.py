"""Anahtar kelime suzgeci (config/anahtar-kelimeler.json).

Topla calistiginda yeni adaylara uygulanir. Kelime listesi degisince tum adaylari yeniden
degerlendirmek icin:  python pipeline/filtre.py
Elenen adaylar silinmez; 'filtre' alaninda nedeniyle birlikte tutulur ve analize gonderilmez.
"""
import glob
import json
import os
import re

KOK = os.path.join(os.path.dirname(__file__), "..")
_HARF = "a-z0-9çğöşü"


PARA_POLITIKASI = re.compile(r"faiz oranlar\w*\s+ilişkin\s+basın\s+duyurusu|para politikası kurulu toplantı özeti", re.I)
PARA_POLITIKASI_NEDEN = "TCMB para politikası duyurusu (süzgeçten muaf)"


def normal(s):
    s = (s or "").replace("İ", "i").replace("I", "i").lower().replace("ı", "i")
    return re.sub(r"[-_/]+", " ", s)


def _desen(terim, tam_kelime):
    t = normal(terim)
    govde = re.escape(t)
    son = rf"(?![{_HARF}])" if len(t) <= 4 or t in tam_kelime else ""
    return re.compile(rf"(?<![{_HARF}]){govde}{son}")


class Suzgec:
    def __init__(self, yol=None):
        yol = yol or os.path.join(KOK, "config", "anahtar-kelimeler.json")
        cfg = json.load(open(yol, encoding="utf-8"))
        tam = {normal(t) for t in cfg.get("tam_kelime", [])}
        self.cekirdek = set(cfg["kural"]["cekirdek_kaynaklar"])
        self.dahil = [(konu, t, _desen(t, tam)) for konu, ts in cfg["dahil"].items() for t in ts]
        self.disla = [(t, _desen(t, tam)) for t in cfg["disla"]]

    def degerlendir(self, aday):
        metin = normal(" ".join([aday.get("baslik_orijinal", ""), aday.get("ozet_kaynak", ""),
                                 aday.get("url", "")]).replace("by default", ""))
        if aday["kurum"] == "tcmb" and PARA_POLITIKASI.search(aday.get("baslik_orijinal", "")):
            return {"sonuc": "gecti", "neden": PARA_POLITIKASI_NEDEN, "konular": ["Diğer"]}
        dis = [t for t, d in self.disla if d.search(metin)]
        konular = sorted({k for k, t, d in self.dahil if d.search(metin)})
        kelimeler = sorted({t for k, t, d in self.dahil if d.search(metin)})[:8]
        if dis:
            sonuc, neden = "elendi", "dışlama: " + ", ".join(dis[:3])
        elif aday["kurum"] in self.cekirdek:
            sonuc, neden = "gecti", "çekirdek kaynak"
        elif konular:
            sonuc, neden = "gecti", "dahil: " + ", ".join(kelimeler[:4])
        else:
            sonuc, neden = "elendi", "dahil kelimesi yok"
        return {"sonuc": sonuc, "neden": neden, "konular": konular}


def hepsini_yenile():
    s = Suzgec()
    sayac = {"gecti": 0, "elendi": 0}
    for yol in glob.glob(os.path.join(KOK, "data", "adaylar", "*.json")):
        kayitlar = json.load(open(yol, encoding="utf-8"))
        for k in kayitlar:
            k["filtre"] = s.degerlendir(k)
            sayac[k["filtre"]["sonuc"]] += 1
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(kayitlar, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print(sayac)


if __name__ == "__main__":
    hepsini_yenile()
