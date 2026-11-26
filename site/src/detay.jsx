import { useEffect } from 'react'
import { kn, tr } from './ortak.js'
import { puanla, puanMetni } from './puan.js'
import { Sev, Etiket, Yildiz, Puan } from './kucuk.jsx'

const BASLIK = ['Yönetici özeti', 'Yayının amacı', 'Önceki çerçeve', 'Yeni hükümler ve değişiklikler', 'Teknik etkiler', 'Operasyonel etki',
  'PD, LGD, EAD ve ECL etkileri', 'Sermaye ve RWA', 'İklim ve sürdürülebilirlik', 'Tarihler', 'Gözden geçirilmesi önerilen alanlar', 'Kaynak ve referanslar']
const KISA = ['Yönetici özeti', 'Yayının amacı', 'Önceki çerçeve', 'Yeni hükümler', 'Teknik etkiler', 'Operasyonel etki', 'PD · LGD · EAD · ECL', 'Sermaye ve RWA', 'İklim ve sürdürülebilirlik', 'Tarihler', 'Gözden geçirilecek alanlar', 'Kaynak ve referanslar']
const DURUMLAR = ['Taslak', 'İstişare', 'Nihai', 'Yürürlükte']
const PC = { 'Yüksek': '#B42318', Orta: '#8A6A00', 'Düşük': '#4A5767' }

function Blok({ b }) {
  if (!b) return <div className="mut">Bilgi yok.</div>
  const tey = b.teyitli || [], olasi = b.olasi_etki || []
  if (!tey.length && !olasi.length) return <div className="mut">{b.ilgili_degil ? 'Bu belge için ilgili değil.' : 'Bilgi yok.'}</div>
  return (
    <>
      {tey.map((t, i) => (
        <div className="hukum" key={i}>
          <div>{t.hukum}</div>
          {t.alinti && <div className="alinti">“{t.alinti}”</div>}
          <div className="mut" style={{ fontSize: 12, marginTop: 2 }}>
            {t.sayfa ? 's. ' + t.sayfa : ''}{t.paragraf ? ', par. ' + t.paragraf : ''}
            {t.alinti_dogrulandi === false && <span style={{ color: '#B42318' }}> · alıntı metinde doğrulanamadı</span>}
          </div>
          <span className="sagalt"><Etiket t="tey" /></span>
        </div>
      ))}
      {olasi.length > 0 && (
        <div className="hukum">
          {olasi.map((t, i) => <div key={i} style={{ marginBottom: 4 }}>{t}</div>)}
          <span className="sagalt"><Etiket t="olasi" /></span>
        </div>
      )}
      {b.karsilastirma_kaynagi === 'genel_bilgi' && <div style={{ fontSize: 12, color: '#7A4E00' }}>Önceki çerçeve belgeden değil, genel bilgiden gelir; teyitli sayılmaz.</div>}
    </>
  )
}

const Bolum = ({ n, children }) => (
  <section id={'s' + n} className="bolum"><h2>{n}. {BASLIK[n - 1]}</h2>{children}</section>
)

export default function Detay({ x, veri, izleme }) {
  useEffect(() => { window.scrollTo(0, 0) }, [x && x.id])
  if (!x) return <div className="w sayfa">Kayıt bulunamadı. <a href="#ana">Genel bakışa dön</a></div>
  const a = x.analiz || {}, ab = x.analiz_bilgisi || {}, P = a.parametre_etkisi || {}
  const p = puanla(x)
  // yayin + yururluk + belgedeki son 3 tarih
  const tarihler = [{ tur: 'Yayın tarihi', tarih: x.yayin_tarihi }]
  if (x.yururluk_tarihi) tarihler.push({ tur: 'Yürürlük', tarih: x.yururluk_tarihi })
  const gorulen = new Set(tarihler.map((t) => t.tur + t.tarih))
  const ek = [...(a.tarihler || [])].filter((t) => t.tarih && !gorulen.has(t.tur + t.tarih))
    .sort((u, v) => v.tarih.localeCompare(u.tarih)).slice(0, 3)
  const benzer = veri.yayinlar.filter((v) => v.id !== x.id && (v.konu === x.konu || v.kurum === x.kurum)).slice(0, 4)
  const sekme = (i) => (e) => { e.preventDefault(); document.getElementById('s' + (i + 1))?.scrollIntoView({ behavior: 'smooth' }) }
  return (
    <>
      <div className="dustu"><div className="w">
        <div className="mut" style={{ fontSize: 13 }}><a href="#ana">Genel Bakış</a> / {x.konu}</div>
        <div className="durum" style={{ gap: '8px 12px' }}>
          <Sev o={x.onem} /><span className="mut">|</span><b>{kn(x.kurum)}</b><span className="rozet">{x.belge_turu}</span><Puan p={p} />
        </div>
        <h1>{x.baslik_tr}</h1>
        <div className="mut" style={{ fontSize: 13 }}>Orijinal başlık: {x.baslik_orijinal}</div>
        <div className="meta">
          <div><div className="mut">Yayın tarihi</div><b>{tr(x.yayin_tarihi)}</b></div>
          <div><div className="mut">Yürürlük</div><b>{x.yururluk_tarihi ? tr(x.yururluk_tarihi) : 'Belirtilmemiş'}</b></div>
          {x.gorus_son_tarihi && <div><div className="mut">Görüş son tarihi</div><b>{tr(x.gorus_son_tarihi)}</b></div>}
          <div className="e">
            <a className="btn" href={x.url} target="_blank" rel="noopener noreferrer">Orijinal belge ↗</a>
            <Yildiz izleme={izleme} id={x.id} />
          </div>
        </div>
        <div className="durum"><span className="mut">Statü:</span>
          {[...DURUMLAR, ...(DURUMLAR.includes(x.statu) ? [] : [x.statu])].map((s) => <span key={s} className={'p' + (s === x.statu ? ' on' : '')}>{s}</span>)}
        </div>
        <div style={{ fontSize: 13, color: '#3D434D' }}><b>Önem gerekçesi:</b> {x.onem_gerekcesi}</div>
        <div className="mut" style={{ fontSize: 12 }}>Puan dağılımı: {puanMetni(p)}</div>
      </div></div>

      <div className="w iki" style={{ paddingTop: 24, paddingBottom: 40 }}>
        <article className="ana" style={{ gap: 20 }}>
          <Bolum n={1}><p style={{ margin: 0, fontSize: 16, lineHeight: 1.65 }}>{a.yonetici_ozeti}</p></Bolum>
          <Bolum n={2}><Blok b={a.amac} /></Bolum>
          <Bolum n={3}><Blok b={a.onceki_cerceve} /></Bolum>
          <Bolum n={4}>
            {(a.degisiklikler || []).length ? (
              <div className="tablo"><table style={{ minWidth: 560 }}>
                <thead><tr><th>Konu</th><th>Önceki</th><th>Yeni</th><th>Kaynak</th></tr></thead>
                <tbody>{a.degisiklikler.map((d, i) => (
                  <tr key={i}><td style={{ fontWeight: 600 }}>{d.konu}</td><td className="mut">{d.onceki}</td>
                    <td style={{ background: '#F2F7F5' }}>{d.yeni}</td><td>{d.referans}</td></tr>))}</tbody>
              </table></div>
            ) : <div className="mut">Belirgin bir değişiklik tespit edilmedi.</div>}
          </Bolum>
          <Bolum n={5}><Blok b={a.teknik_etkiler} /></Bolum>
          <Bolum n={6}><Blok b={a.operasyonel_etki} /></Bolum>
          <Bolum n={7}>
            <div className="etk">
              <div className="param">{['PD', 'LGD', 'EAD', 'ECL'].map((k) => {
                const m = P[k] || {}
                return (<div key={k}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                    <span className="serif" style={{ fontSize: 22, fontWeight: 600 }}>{k}</span>
                    <span style={{ fontSize: 12, fontWeight: 600, color: PC[m.duzey] || '#4A5767' }}>{m.duzey || '—'}</span></div>
                  <div style={{ fontSize: 13, color: '#3D434D', marginTop: 6 }}>{m.not}</div></div>)
              })}</div>
              <span className="sagalt"><Etiket t="olasi" /></span>
            </div>
          </Bolum>
          <Bolum n={8}><Blok b={a.sermaye_rwa} /></Bolum>
          <Bolum n={9}><Blok b={a.iklim} /></Bolum>
          <Bolum n={10}>
            {[...tarihler, ...ek].map((t, i) => (
              <div key={i} style={{ display: 'flex', justifyContent: 'space-between', padding: '8px 0', borderTop: i ? '1px solid #EEEAE2' : 0 }}>
                <span>{t.tur}</span><span><b>{tr(t.tarih)}</b> {t.referans && <span className="mut" style={{ fontSize: 12 }}>{t.referans}</span>}</span>
              </div>))}
            {!x.yururluk_tarihi && !ek.length && <div className="mut" style={{ marginTop: 6 }}>Belgede başka tarih belirtilmemiş.</div>}
          </Bolum>
          <Bolum n={11}>
            <div className="etk">
              {(a.gozden_gecirilecekler || []).map((r, i) => (
                <div key={i} style={{ display: 'flex', gap: 14, padding: '10px 0', borderTop: i ? '1px solid #EEEAE2' : 0 }}>
                  <span className="serif" style={{ fontWeight: 600, color: '#0B5D52', width: 20 }}>{i + 1}</span>
                  <div><div style={{ fontWeight: 600 }}>{r.baslik}</div><div className="mut" style={{ fontSize: 13 }}>{r.aciklama}</div></div>
                </div>))}
              {!(a.gozden_gecirilecekler || []).length && <div className="mut">Öneri yok.</div>}
              <span className="sagalt"><Etiket t="olasi" /></span>
            </div>
          </Bolum>
          <Bolum n={12}>
            {(a.referanslar || []).map((r, i) => <div key={i} style={{ padding: '4px 0' }}>{r.metin} <span className="mut" style={{ fontSize: 12 }}>{r.sayfa ? 's. ' + r.sayfa : ''}</span></div>)}
            <div style={{ marginTop: 8 }}><a href={x.url} target="_blank" rel="noopener noreferrer">Orijinal belge ↗</a></div>
          </Bolum>
          {benzer.length > 0 && <section className="bolum"><h2 style={{ fontSize: 18 }}>İlgili yayınlar</h2>
            {benzer.map((v) => <div key={v.id} style={{ padding: '4px 0' }}><a href={'#y-' + v.id}>{kn(v.kurum)} · {v.baslik_tr}</a></div>)}</section>}
          <div className="altbilgi">
            Analiz bilgisi: {ab.model} · {String(ab.olusturma_zamani || '').slice(0, 16).replace('T', ' ')} · Doğrulanan alıntı {ab.alinti_dogrulanan}/{ab.alinti_toplam} · Güven: {ab.guven}
            {'  ·  '}<span className="etiket tey">TEYİTLİ</span> belgedeki hüküm <span className="etiket olasi">OLASI ETKİ</span> yapay zekâ yorumu
          </div>
        </article>
        <nav className="toc" aria-label="Analiz bölümleri">
          <div className="mut" style={{ fontSize: 12, letterSpacing: '.04em', textTransform: 'uppercase', marginBottom: 6 }}>Analiz</div>
          {KISA.map((t, i) => <a key={i} href={'#s' + (i + 1)} onClick={sekme(i)}><span style={{ color: '#8B919B', width: 18 }}>{i + 1}</span>{t}</a>)}
        </nav>
      </div>
    </>
  )
}
