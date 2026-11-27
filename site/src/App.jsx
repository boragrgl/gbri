import { useEffect, useLayoutEffect, useRef, useState, useCallback } from 'react'
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


const Zil = () => (<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>)
const Ayar = () => (<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M4 6h8M18 6h2M4 12h2M12 12h8M4 18h10M20 18h0"/><circle cx="15" cy="6" r="2.2"/><circle cx="9" cy="12" r="2.2"/><circle cx="17" cy="18" r="2.2"/></svg>)

function Ikonlar() {
  const [acik, setAcik] = useState(null)
  const ac = (k) => setAcik((o) => (o === k ? null : k))
  return (
    <div className="ikonlar">
      <button type="button" className={'ikon' + (acik === 'bildirim' ? ' on' : '')} aria-label="Bildirimler" aria-expanded={acik === 'bildirim'} onClick={() => ac('bildirim')}><Zil /><span className="nokta" /></button>
      <button type="button" className={'ikon' + (acik === 'ayar' ? ' on' : '')} aria-label="Ayarlar" aria-expanded={acik === 'ayar'} onClick={() => ac('ayar')}><Ayar /></button>
      {acik && <div className="perde" onClick={() => setAcik(null)} />}
      {acik === 'bildirim' && (
        <div className="acilir" role="dialog" aria-label="Bildirimler">
          <b>Bildirimler</b>
          <div className="mut" style={{ fontSize: 13, margin: '6px 0 10px' }}>Yeni kritik yayınlar burada listelenecek.</div>
          <div className="pasif">Henüz bildirim yok</div>
          <div className="mut" style={{ fontSize: 12, marginTop: 10 }}>Bu bölüm sonraki sürümde açılacak.</div>
        </div>)}
      {acik === 'ayar' && (
        <div className="acilir" role="dialog" aria-label="Ayarlar">
          <b>Ayarlar</b>
          {[['Dil', 'Türkçe'], ['Görünüm', 'Açık tema'], ['Bildirim tercihleri', 'Kapalı'], ['Önem eşiği', 'Tümü']].map(([a, d]) => (
            <label key={a} className="ayarsatir"><span>{a}</span><select disabled><option>{d}</option></select></label>))}
          <div className="mut" style={{ fontSize: 12, marginTop: 10 }}>Ayarlar sonraki sürümde etkinleşecek.</div>
        </div>)}
    </div>
  )
}

function KonuSatiri({ konu, q, setQ }) {
  const kap = useRef(null), olcu = useRef(null)
  const [n, setN] = useState(KONULAR.length)
  const [ac, setAc] = useState(false)
  useLayoutEffect(() => {
    const hesapla = () => {
      if (!kap.current || !olcu.current) return
      const w = [...olcu.current.children].map((c) => c.getBoundingClientRect().width + 8)
      const masa = window.innerWidth > 720
      const bos = kap.current.clientWidth - (masa ? 64 : 32) - (masa ? 90 : 0) - (masa ? 270 : 0) - 96
      let top = 0, say = 0
      for (const v of w) { if (top + v > bos) break; top += v; say++ }
      setN(say)
    }
    hesapla(); window.addEventListener('resize', hesapla); return () => window.removeEventListener('resize', hesapla)
  }, [])
  const gor = KONULAR.slice(0, n), gizli = KONULAR.slice(n)
  const pil = (k) => <a key={k.slug} className={'pill' + (konu && konu.slug === k.slug ? ' on' : '')} href={konu && konu.slug === k.slug ? '#ana' : '#konu-' + k.slug} onClick={() => setAc(false)}>{k.ad}</a>
  return (
    <div className="w konusatir" ref={kap}>
      <span className="konuetiket">KONULAR</span>
      {gor.map(pil)}
      {gizli.length > 0 && (
        <span className="digerkonu">
          <button type="button" className={'pill' + (gizli.some((k) => konu && konu.slug === k.slug) ? ' on' : '')} aria-expanded={ac} onClick={() => setAc(!ac)}>Diğer ({gizli.length}) ▾</button>
          {ac && <><div className="perde" onClick={() => setAc(false)} /><div className="acilir sol">{gizli.map((k) => <a key={k.slug} href={'#konu-' + k.slug} onClick={() => setAc(false)} style={{ padding: '7px 4px', display: 'block' }}>{k.ad}</a>)}</div></>}
        </span>)}
      <div ref={olcu} className="olcu" aria-hidden="true">{KONULAR.map((k) => <span key={k.slug} className="pill">{k.ad}</span>)}</div>
      <div style={{ flex: 1 }} />
      <label htmlFor="ara" style={{ position: 'absolute', left: -9999 }}>Ara</label>
      <input id="ara" className="ara" type="search" placeholder="Yayın, kurum veya konu ara" value={q} onChange={(e) => setQ(e.target.value)} />
    </div>
  )
}

function YukariDugmesi() {
  const [g, setG] = useState(false)
  useEffect(() => { const f = () => setG(window.scrollY > 300); f(); window.addEventListener('scroll', f, { passive: true }); return () => window.removeEventListener('scroll', f) }, [])
  if (!g) return null
  return <button type="button" className="yukari" aria-label="Sayfanın başına dön" title="Sayfanın başına dön" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>↑</button>
}

export function Uygulama({ veri, rota, izleme, q = '', setQ = () => {} }) {
  const [, tip, ek] = /^([a-z0-9]+)(?:-(.+))?$/.exec(rota || 'ana') || []
  const konu = tip === 'konu' ? KONULAR.find((k) => k.slug === ek) : null
  const suz = (l) => l.filter((x) => !q || (x.baslik_tr + ' ' + x.kurum + ' ' + x.konu + ' ' + (x.alt_konular || []).join(' ')).toLowerCase().includes(q.toLowerCase()))
  const tum = suz(veri.yayinlar)
  const liste = konu ? tum.filter((x) => (konu.eslesir ? konu.eslesir(x) : x.konu === konu.anahtar)) : tum
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
          <Ikonlar />
        </div>
        <div className="konubar"><KonuSatiri konu={konu} q={q} setQ={setQ} /></div>
      </header>
      <div className="tarihsatir"><div className="w" style={{ justifyContent: 'flex-end' }}><span>{trUzun(bugun())}</span></div></div>
      {sayfa}
      <div className="w sayfasonu"><button type="button" className="btn2" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>↑ Sayfa başına dön</button></div>
      <YukariDugmesi />
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
