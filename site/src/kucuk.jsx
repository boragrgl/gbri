import { useLayoutEffect, useRef, useState } from 'react'
import { RENK, kn, tr, trKisa } from './ortak.js'
import { puanMetni } from './puan.js'

export const Sev = ({ o }) => (
  <span className="sev" style={{ color: RENK[o] }}><i style={{ background: RENK[o] }} />{o}</span>
)
export const Puan = ({ p }) => <span className="puan" title={puanMetni(p)}>Puan {p.toplam}</span>
export const Etiket = ({ t }) =>
  t === 'tey' ? <span className="etiket tey">TEYİTLİ</span> : <span className="etiket olasi">OLASI ETKİ</span>

export function Yildiz({ izleme, id }) {
  const on = izleme.yayin.includes(id)
  return (
    <button type="button" className={'yildiz' + (on ? ' on' : '')} aria-pressed={on}
      onClick={(e) => { e.preventDefault(); izleme.degistir('yayin', id) }}>
      {on ? '★ İzleniyor' : '☆ İzle'}
    </button>
  )
}

export function Kart({ x, p, izleme }) {
  return (
    <a className="kart" href={'#y-' + x.id}>
      <div className="kartust">
        <Sev o={x.onem} /><span className="mut">|</span><b>{kn(x.kurum)}</b>
        <span className="rozet">{x.statu}</span>
        {p && <Puan p={p} />}
        <span className="sag">{tr(x.yayin_tarihi)}</span>
      </div>
      <h3 className="serif">{x.baslik_tr}</h3>
      <p>{x.ozet_tek_satir}</p>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginTop: 10, alignItems: 'center' }}>
        <span className="mut" style={{ fontSize: 12 }}>Etkilenen:</span>
        {(x.etkilenen_alanlar || []).map((t) => <span className="chip" key={t}>{t}</span>)}
        {izleme && <span style={{ marginLeft: 'auto' }}><Yildiz izleme={izleme} id={x.id} /></span>}
      </div>
    </a>
  )
}

export function Tablo({ liste, puanlar }) {
  return (
    <div className="card tablo">
      <table style={{ minWidth: 820 }}>
        <thead><tr><th>Önem</th>{puanlar && <th>Puan</th>}<th>Kurum</th><th>Başlık</th><th>Tür</th><th>Statü</th><th>Yayın</th></tr></thead>
        <tbody>
          {liste.map((x) => (
            <tr key={x.id}>
              <td><Sev o={x.onem} /></td>
              {puanlar && <td>{puanlar(x).toplam}</td>}
              <td style={{ fontWeight: 600 }}>{kn(x.kurum)}</td>
              <td><a href={'#y-' + x.id}>{x.baslik_tr}</a></td>
              <td className="mut">{x.belge_turu}</td><td>{x.statu}</td>
              <td className="mut" style={{ whiteSpace: 'nowrap' }}>{trKisa(x.yayin_tarihi)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export const Bos = ({ children }) => <div className="card mut">{children}</div>

// Tek satirlik secenek cubugu: sigmayanlar "Diger" acilirina gider.
export function TekSatir({ ogeler, secili, sec, etiket }) {
  const kap = useRef(null), olcu = useRef(null)
  const [n, setN] = useState(ogeler.length)
  const [ac, setAc] = useState(false)
  useLayoutEffect(() => {
    const hesapla = () => {
      if (!kap.current || !olcu.current) return
      const w = [...olcu.current.children].map((c) => c.getBoundingClientRect().width + 8)
      const bos = kap.current.clientWidth - w[0] - 110
      let top = 0, say = 0
      for (const v of w.slice(1)) { if (top + v > bos) break; top += v; say++ }
      setN(say)
    }
    hesapla(); window.addEventListener('resize', hesapla); return () => window.removeEventListener('resize', hesapla)
  }, [ogeler.length])
  const gor = ogeler.slice(0, n), gizli = ogeler.slice(n)
  const dugme = (o) => <button key={o.k} className={secili === o.k ? 'on' : ''} onClick={() => { sec(secili === o.k ? '' : o.k); setAc(false) }}>{o.etiket}</button>
  return (
    <div className="altkonu" ref={kap} role="group" aria-label={etiket}>
      <button className={!secili ? 'on' : ''} onClick={() => sec('')}>Tümü</button>
      {gor.map(dugme)}
      {gizli.length > 0 && (
        <span style={{ position: 'relative', flex: 'none' }}>
          <button className={gizli.some((o) => o.k === secili) ? 'on' : ''} aria-expanded={ac} onClick={() => setAc(!ac)}>Diğer ({gizli.length}) ▾</button>
          {ac && <><div className="perde" onClick={() => setAc(false)} /><div className="acilir sol" style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
            {gizli.map((o) => <button key={o.k} className={'acilirogesi' + (secili === o.k ? ' on' : '')} onClick={() => { sec(secili === o.k ? '' : o.k); setAc(false) }}>{o.etiket}</button>)}</div></>}
        </span>)}
      <div className="olcu" ref={olcu} aria-hidden="true"><button>Tümü</button>{ogeler.map((o) => <button key={o.k}>{o.etiket}</button>)}</div>
    </div>
  )
}
