// Onem puani: 0-100. Siralama ve "Onemli degisiklikler" bolumu bunu kullanir.
const ONEM = { Kritik: 55, 'Yüksek': 40, Orta: 22, 'Düşük': 8 }
const GUVEN = { 'Yüksek': 10, Orta: 5, 'Düşük': 0 }
const gun = (a, b) => Math.round((new Date(a) - new Date(b)) / 86400000)
export function bugun() { return new Date().toISOString().slice(0, 10) }
export function puanla(x, t = bugun()) {
  const onem = ONEM[x.onem] ?? 8
  const ileri = [x.gorus_son_tarihi, x.yururluk_tarihi, x.uyum_son_tarihi].filter((d) => d && d >= t).map((d) => gun(d, t))
  const tarih = ileri.length ? Math.round(20 * Math.max(0, 1 - Math.min(...ileri) / 60)) : 0
  const yenilik = Math.round(15 * Math.max(0, 1 - Math.max(0, gun(t, x.yayin_tarihi)) / 30))
  const guven = GUVEN[x.analiz_bilgisi?.guven] ?? 0
  return { toplam: onem + tarih + yenilik + guven, onem, tarih, yenilik, guven }
}
export const puanMetni = (p) => `Önem ${p.onem} · Tarih ${p.tarih} · Yenilik ${p.yenilik} · Güven ${p.guven}`
