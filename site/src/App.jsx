import { useEffect, useState, useCallback } from 'react'
import { KONULAR, trUzun } from './ortak.js'
import { bugun } from './puan.js'
import Detay from './detay.jsx'
import { Genel, Gunluk, Onemli, Takvim, Arsiv, Kurumlar, Kurum, Izleme } from './sayfalar.jsx'

const MENU = [['ana', 'Genel Bakış'], ['gunluk', 'Günlük Yayınlar'], ['onemli', 'Önemli Değişiklikler'], ['takvim', 'Takvim'], ['arsiv', 'Arşiv'], ['kurumlar', 'Kurumlar'], ['izleme', 'İzleme Listem']]

function useIzleme() {
  const oku = () => { try { return { yayin: [], kurum: [], ...JSON.parse(localStorage.getItem('gbri-izleme') || '{}') } } catch { return { yayin: [], kurum: [] } } }
  const [d, setD] = useState({ yayin: [], kurum: [] })
  useEffect(() => { setD(oku()) }, [])
  const degistir = useCallback((tur, id) => setD((o) => {
    const n = { ...o, [tur]: o[tur].includes(id) ? o[tur].filter((v) => v !== id) : [...o[tur], id] }
    try { localStorage.setItem('gbri-izleme', JSON.stringify(n)) } catch { /* depolama kapalı */ }
    return n
  }), [])
  return { ...d, degistir }
}

export function Uygulama({ veri, rota, izleme, q = '', setQ = () => {} }) {
  const [, tip, ek] = /^([a-z0-9]+)(?:-(.+))?$/.exec(rota || 'ana') || []
  const konu = tip === 'konu' ? KONULAR.find((k) => k.slug === ek) : null
  const suz = (l) => l.filter((x) => !q || (x.baslik_tr + ' ' + x.kurum + ' ' + x.konu + ' ' + (x.alt_konular || []).join(' ')).toLowerCase().includes(q.toLowerCase()))
  const tum = suz(veri.yayinlar)
  const liste = konu ? tum.filter((x) => x.konu === konu.anahtar) : tum
  const aktif = tip === 'y' ? 'ana' : tip === 'konu' ? 'ana' : tip === 'kurum' ? 'kurumlar' : tip
  let sayfa
  if (tip === 'y') sayfa = <Detay x={veri.yayinlar.find((x) => x.id === ek)} veri={veri} izleme={izleme} />
  else if (tip === 'gunluk') sayfa = <Gunluk liste={tum} izleme={izleme} />
  else if (tip === 'onemli') sayfa = <Onemli liste={tum} izleme={izleme} />
  else if (tip === 'takvim') sayfa = <Takvim veri={veri} />
  else if (tip === 'arsiv') sayfa = <Arsiv liste={tum} veri={veri} q={q} />
  else if (tip === 'kurumlar') sayfa = <Kurumlar veri={veri} izleme={izleme} />
  else if (tip === 'kurum') sayfa = <Kurum id={ek} veri={veri} izleme={izleme} />
  else if (tip === 'izleme') sayfa = <Izleme veri={veri} izleme={izleme} />
  else sayfa = <Genel konu={konu} liste={liste} veri={veri} izleme={izleme} key={konu ? konu.slug : 'ana'} />
  return (
    <>
      <header className="ust">
        <div className="w satir">
          <a className="logo" href="#ana"><b>GBRI</b><span>Bankacılık Düzenleme İstihbaratı</span></a>
          <nav className="menu" aria-label="Ana menü">
            {MENU.map(([r, ad]) => <a key={r} href={'#' + r} className={aktif === r ? 'on' : ''}>{ad}</a>)}
          </nav>
        </div>
        <div className="konubar"><div className="w satir">
          <span style={{ fontSize: 12, color: '#9AA0A8', marginRight: 8 }}>KONULAR</span>
          {KONULAR.map((k) => <a key={k.slug} className={'pill' + (konu && konu.slug === k.slug ? ' on' : '')} style={{ textDecoration: 'none' }}
            href={konu && konu.slug === k.slug ? '#ana' : '#konu-' + k.slug}>{k.ad}</a>)}
          <div style={{ flex: 1 }} />
          <label htmlFor="ara" style={{ position: 'absolute', left: -9999 }}>Ara</label>
          <input id="ara" className="ara" type="search" placeholder="Yayın, kurum veya konu ara" value={q} onChange={(e) => setQ(e.target.value)} />
        </div></div>
      </header>
      <div className="tarihsatir"><div className="w"><span>Önizleme sürümü · son 1 aylık deneme verisi</span><span>{trUzun(bugun())}</span></div></div>
      {sayfa}
    </>
  )
}

export default function App() {
  const [veri, setVeri] = useState(null)
  const [hata, setHata] = useState(null)
  const [rota, setRota] = useState(() => (typeof location !== 'undefined' ? location.hash.slice(1) : '') || 'ana')
  const [q, setQ] = useState('')
  const izleme = useIzleme()
  useEffect(() => {
    const f = (a) => fetch(import.meta.env.BASE_URL + 'data/' + a + '.json').then((r) => { if (!r.ok) throw new Error(a); return r.json() })
    Promise.all([f('yayinlar'), f('adaylar'), f('kaynaklar')]).then(([yayinlar, adaylar, kaynaklar]) => setVeri({ yayinlar, adaylar, kaynaklar })).catch((e) => setHata(String(e)))
  }, [])
  useEffect(() => {
    const h = () => { const r = location.hash.slice(1) || 'ana'; if (/^s\d+$/.test(r)) return; setRota(r); window.scrollTo(0, 0) }
    window.addEventListener('hashchange', h); return () => window.removeEventListener('hashchange', h)
  }, [])
  if (hata) return <div className="w sayfa">Veri yüklenemedi ({hata}). Sayfayı yenileyin.</div>
  if (!veri) return <div className="w sayfa mut">Yükleniyor…</div>
  return <Uygulama veri={veri} rota={rota} izleme={izleme} q={q} setQ={setQ} />
}
