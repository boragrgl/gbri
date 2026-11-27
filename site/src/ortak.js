export const RENK = { Kritik: '#B42318', 'Yüksek': '#B54708', Orta: '#8A6A00', 'Düşük': '#4A5767' }
export const KURUM = { bddk: 'BDDK', tcmb: 'TCMB', kgk: 'KGK', spk: 'SPK', resmigazete: 'Resmî Gazete', eba: 'EBA', ecb: 'ECB', bis: 'BIS', bcbs: 'BCBS', ifrs: 'IFRS', issb: 'ISSB', fsb: 'FSB', worldbank: 'Dünya Bankası', oecd: 'OECD' }
export const kn = (k) => KURUM[k] || String(k).toUpperCase()
export const AY = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara']
export const AYUZUN = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
export const GUNLER = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi']
export const tr = (d) => { if (!d) return '—'; const [y, m, g] = d.split('-'); return `${+g} ${AY[+m - 1]} ${y}` }
export const trKisa = (d) => { const [, m, g] = d.split('-'); return `${+g} ${AY[+m - 1]}` }
export const trUzun = (d) => { const t = new Date(d + 'T12:00:00'); return `${t.getDate()} ${AYUZUN[t.getMonth()]} ${t.getFullYear()} · ${GUNLER[t.getDay()]}` }
export const KURUM_TAM = { ecb: 'European Central Bank', fsb: 'Financial Stability Board', bis: 'Bank for International Settlements', bcbs: 'Basel Committee on Banking Supervision', eba: 'European Banking Authority', ifrs: 'IFRS Foundation', issb: 'International Sustainability Standards Board', worldbank: 'World Bank', bddk: 'Bankacılık Düzenleme ve Denetleme Kurumu', tcmb: 'Türkiye Cumhuriyet Merkez Bankası', kgk: 'Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu', spk: 'Sermaye Piyasası Kurulu', resmigazete: 'T.C. Resmî Gazete', oecd: 'Organisation for Economic Co-operation and Development', imf: 'International Monetary Fund' }
const metin = (x) => [x.baslik_tr, x.baslik_orijinal, x.ozet_tek_satir, (x.alt_konular || []).join(' '), (x.etkilenen_alanlar || []).join(' ')].join(' ')
export const KONULAR = [
  { slug: 'tfrs9', ad: 'TFRS 9 / IFRS 9', anahtar: 'TFRS 9' },
  { slug: 'sermaye', ad: 'Sermaye', anahtar: 'Basel', eslesir: (x) => x.konu === 'Basel' || /sermaye|capital|\brwa\b|basel/i.test(metin(x)) },
  { slug: 'surdurulebilirlik', ad: 'Sürdürülebilirlik ve ESG', anahtar: 'Sürdürülebilirlik' },
  { slug: 'risk', ad: 'Risk Yönetimi', anahtar: 'Risk Yönetimi' },
]
export const ONEMSIRA = { Kritik: 0, 'Yüksek': 1, Orta: 2, 'Düşük': 3 }
