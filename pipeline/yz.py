"""Gemini istemcisi: model secimi, yeniden deneme, JSON ayristirma."""
import json
import os
import re
import time
import urllib.error
import urllib.request

API = "https://generativelanguage.googleapis.com/v1beta"
TERCIH = ["gemini-3-flash-preview", "gemini-flash-latest", "gemini-3.1-flash-lite",
          "gemini-flash-lite-latest", "gemini-2.5-flash-lite", "gemini-2.5-flash"]


class Kota(Exception):
    pass


class YZ:
    def __init__(self):
        self.anahtar = os.environ["GEMINI_API_KEY"]
        self.modeller = list(TERCIH)
        self.model = None
        self.cagri = 0
        self.son = 0.0

    def _istek(self, model, sistem, kullanici, sicaklik):
        govde = json.dumps({
            "systemInstruction": {"parts": [{"text": sistem}]},
            "contents": [{"role": "user", "parts": [{"text": kullanici}]}],
            "generationConfig": {"temperature": sicaklik, "responseMimeType": "application/json"}}).encode()
        req = urllib.request.Request(f"{API}/models/{model}:generateContent", data=govde,
                                     headers={"x-goog-api-key": self.anahtar, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=240) as r:
            out = json.loads(r.read())
        parcalar = out["candidates"][0]["content"]["parts"]
        return "".join(p.get("text", "") for p in parcalar), out.get("usageMetadata", {})

    def json_iste(self, sistem, kullanici, sicaklik=0.1, aralik=7.0):
        """JSON nesnesi doner. Gecici hatalarda bekler, model yetersizse siradakine gecer."""
        hata = None
        for tur in range(len(self.modeller) * 3 + 3):
            if not self.modeller:
                break
            model = self.model or self.modeller[0]
            bekle = aralik - (time.time() - self.son)
            if bekle > 0:
                time.sleep(bekle)
            try:
                self.son = time.time()
                self.cagri += 1
                metin, kullanim = self._istek(model, sistem, kullanici, sicaklik)
                self.model = model
                return self._ayristir(metin), model, kullanim
            except urllib.error.HTTPError as e:
                govde = e.read()[:500].decode("utf-8", "replace")
                hata = f"HTTP {e.code}: {govde[:200]}"
                print("  yz hata:", model, hata.replace("\n", " "), flush=True)
                if e.code in (404, 400) or ("limit: 0" in govde):
                    self._model_birak(model)
                elif e.code == 429:
                    if "PerDay" in govde or "per day" in govde.lower():
                        self._model_birak(model)
                    else:
                        time.sleep(45)
                else:
                    time.sleep(20 * (1 + tur % 3))
            except (ValueError, KeyError, IndexError) as e:
                hata = f"ayristirma: {type(e).__name__}: {e}"
                print("  yz ayristirma hatasi:", hata, flush=True)
                sicaklik = min(0.4, sicaklik + 0.15)
            except Exception as e:
                hata = f"{type(e).__name__}: {e}"
                print("  yz baglanti hatasi:", hata[:200], flush=True)
                time.sleep(15)
        raise Kota(hata or "model yok")

    def _model_birak(self, model):
        if model in self.modeller:
            self.modeller.remove(model)
        if self.model == model:
            self.model = None

    @staticmethod
    def _ayristir(metin):
        m = metin.strip()
        m = re.sub(r"^```(?:json)?\s*|\s*```$", "", m)
        return json.loads(m)
