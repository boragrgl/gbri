export const RENK = { Kritik: '#B42318', 'Yüksek': '#B54708', Orta: '#8A6A00', 'Düşük': '#4A5767' }
export const KURUM = { bddk: 'BDDK', tcmb: 'TCMB', kgk: 'KGK', spk: 'SPK', resmigazete: 'Resmî Gazete', eba: 'EBA', ecb: 'ECB', bis: 'BIS', bcbs: 'BCBS', ifrs: 'IFRS', issb: 'ISSB', fsb: 'FSB', worldbank: 'Dünya Bankası', oecd: 'OECD' }
export const kn = (k) => KURUM[k] || String(k).toUpperCase()
export const AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara']
export const AYUZUN = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
export const GUNLER = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi']
export const tr = (d) => { if (!d) return '—'; const [y, m, g] = d.split('-'); return `${+g} ${AY[+m - 1]} ${y}` }
export const trKisa = (d) => { const [, m, g] = d.split('-'); return `${+g} ${AY[+m - 1]}` }
export const trUzun = (d) => { const t = new Date(d + 'T12:00:00'); return `${t.getDate()} ${AYUZUN[t.getMonth()]} ${t.getFullYear()} · ${GUNLER[t.getDay()]}` }
export const KONULAR = [
  { slug: 'tfrs9', ad: 'TFRS 9 / IFRS 9', anahtar: 'TFRS 9' },
  { slug: 'basel', ad: 'Basel', anahtar: 'Basel' },
  { slug: 'surdurulebilirlik', ad: 'Sürdürülebilirlik ve ESG', anahtar: 'Sürdürülebilirlik' },
  { slug: 'risk', ad: 'Risk Yönetimi', anahtar: 'Risk Yönetimi' },
]
export const ONEMSIRA = { Kritik: 0, 'Yüksek': 1, Orta: 2, 'Düşük': 3 }
