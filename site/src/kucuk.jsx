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
