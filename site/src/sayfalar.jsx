import { useMemo, useState } from 'react'
import { kn, tr, trKisa, trUzun, AY, AYUZUN, KONULAR, ONEMSIRA } from './ortak.js'
import { puanla, bugun } from './puan.js'
import { Kart, Tablo, Bos, Sev, Yildiz } from './kucuk.jsx'

const puanSirala = (l, t) => [...l].map((x) => ({ x, p: puanla(x, t) }))
  .sort((a, b) => b.p.toplam - a.p.toplam || b.x.yayin_tarihi.localeCompare(a.x.yayin_tarihi))

function yaklasan(liste, t) {
  const o = []
  liste.forEach((x) => [['gorus_son_tarihi', 'Görüş son tarihi'], ['yururluk_tarihi', 'Yürürlük'], ['uyum_son_tarihi', 'Uyum']]
    .forEach(([f, n]) => { if (x[f]) o.push({ d: x[f], n, x }) }))
  return o.sort((a, b) => a.d.localeCompare(b.d)).filter((v) => v.d >= t)
}

export function Genel({ konu, liste, veri, izleme }) {
  const t = bugun()
  const [alt, setAlt] = useState('')
  const l = alt ? liste.filter((x) => (x.alt_konular || []).includes(alt)) : liste
  const k = l.filter((x) => x.onem === 'Kritik').length, y = l.filter((x) => x.onem === 'Yüksek').length
  const sirali = useMemo(() => puanSirala(l, t), [l, t])
  const onem = sirali.slice(0, 5)
  const tar = yaklasan(l, t)
  const dagilim = {}; l.forEach((x) => { dagilim[x.konu] = (dagilim[x.konu] || 0) + 1 })
  const mx = Math.max(1, ...Object.values(dagilim))
  const altlar = {}; liste.forEach((x) => (x.alt_konular || []).forEach((a) => { altlar[a] = (altlar[a] || 0) + 1 }))
  const altListe = Object.entries(altlar).sort((a, b) => b[1] - a[1]).slice(0, 10)
  const baslik = konu ? `${konu.ad} konusunda: ${k} kritik, ${y} yüksek öncelikli gelişme` : `Özet: ${k} kritik, ${y} yüksek öncelikli gelişme`
  return (
    <main className="w sayfa">
      <section>
        <h1 className="buyuk" style={{ fontSize: 38, lineHeight: 1.15 }}>{baslik}</h1>
        <p className="mut" style={{ margin: '12px 0 0', fontSize: 16, maxWidth: 760 }}>
          Son bir aylık deneme verisi. Değişiklikler, bankacılık faaliyetlerine olası etkiyi gösteren bir puana (0–100) göre sıralanır.
        </p>
      </section>
      {konu && altListe.length > 0 && (
        <div className="altkonu" role="group" aria-label="Alt konular">
          <button className={!alt ? 'on' : ''} onClick={() => setAlt('')}>Tümü</button>
          {altListe.map(([a, n]) => <button key={a} className={alt === a ? 'on' : ''} onClick={() => setAlt(alt === a ? '' : a)}>{a} ({n})</button>)}
        </div>)}
      <section className="kpi" aria-label="Özet göstergeler">
        {[['Kritik', k, '#B42318', 'son 1 ay'], ['Yüksek', y, '#B54708', 'son 1 ay'], ['Analiz edilen yayın', l.length, '#15191F', 'toplam'], ['Yaklaşan tarih', tar.length, '#15191F', 'görüş / yürürlük / uyum']]
          .map(([a, n, c, s]) => <div key={a}><div className="mut" style={{ fontSize: 13 }}>{a}</div>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginTop: 4 }}><span className="n" style={{ color: c }}>{n}</span><span className="mut" style={{ fontSize: 13 }}>{s}</span></div></div>)}
      </section>
      <div className="iki">
        <section className="ana">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', flexWrap: 'wrap', gap: 8 }}>
            <h2 style={{ fontSize: 24 }}>Önemli değişiklikler</h2><a href="#onemli">Tümü, puana göre →</a></div>
          {onem.length ? onem.map(({ x, p }) => <Kart key={x.id} x={x} p={p} izleme={izleme} />) : <Bos>Bu süzgeçte yayın yok.</Bos>}
        </section>
        <aside className="yan">
          <section className="card"><h2 style={{ fontSize: 20 }}>Yaklaşan tarihler</h2>
            <div className="mut" style={{ fontSize: 12, margin: '4px 0 10px' }}>Yürürlük, uyum ve görüş bildirme</div>
            {tar.slice(0, 6).map((v, i) => (
              <a key={i} className="tarihkutu" href={'#y-' + v.x.id}>
                <div className="g"><b>{+v.d.slice(8)}</b><span>{AY[+v.d.slice(5, 7) - 1]} {v.d.slice(0, 4)}</span></div>
                <div style={{ minWidth: 0 }}><div className="mut" style={{ fontSize: 12 }}>{v.n} · {kn(v.x.kurum)}</div><div style={{ fontWeight: 500, lineHeight: 1.4 }}>{v.x.baslik_tr}</div></div></a>))}
            {!tar.length && <div className="mut">Yaklaşan tarih yok.</div>}
            <a href="#takvim" style={{ fontSize: 13, display: 'inline-block', marginTop: 8 }}>Takvimi aç →</a></section>
          <section className="card"><h2 style={{ fontSize: 20, marginBottom: 8 }}>Konulara göre dağılım</h2>
            {Object.entries(dagilim).sort((a, b) => b[1] - a[1]).map(([n, c]) => (
              <div key={n} style={{ padding: '6px 0' }}><div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13 }}><span>{n}</span><b>{c}</b></div>
                <div className="cubuk"><div style={{ width: (c / mx * 100) + '%' }} /></div></div>))}</section>
          <section className="card"><h2 style={{ fontSize: 20, marginBottom: 10 }}>Kaynak durumu</h2>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
              {veri.kaynaklar.map((s) => (
                <a key={s.id} className="kaynak" href={'#kurum-' + s.id} title={'Bu kaynaktan toplanan tüm haberler'}>
                  <i style={{ background: !s.aktif ? '#9AA0A8' : s.ardisik_hata ? '#B42318' : '#1F7A4D' }} />{s.ad}</a>))}</div>
            <div className="mut" style={{ fontSize: 12, marginTop: 10 }}>Bir kaynağa tıklayarak ondan toplanan tüm haberleri görebilirsin. Gri: ilk sürümde kapsam dışı.</div></section>
        </aside>
      </div>
      <section style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        <h2 style={{ fontSize: 24 }}>Tüm yayınlar</h2>
        <Tablo liste={[...l].sort((a, b) => b.yayin_tarihi.localeCompare(a.yayin_tarihi))} />
      </section>
      <div className="alt"><span>Yapay zekâ analizleri yorum niteliğindedir; resmî düzenleyici beyanı yerine geçmez. Bağlayıcı metin için orijinal belgeye başvurun.</span>
        <span>{veri.adaylar.filter((a) => a.durum === 'ilgisiz').length} ilgisiz bulunan belge listelerde gösterilmez.</span></div>
    </main>
  )
}

export function Gunluk({ liste, izleme }) {
  const gruplar = {}
  ;[...liste].sort((a, b) => b.yayin_tarihi.localeCompare(a.yayin_tarihi) || ONEMSIRA[a.onem] - ONEMSIRA[b.onem]).forEach((x) => (gruplar[x.yayin_tarihi] ||= []).push(x))
  return (
    <main className="w sayfa"><section><h1 className="buyuk" style={{ fontSize: 34 }}>Günlük yayınlar</h1><p className="mut" style={{ margin: '8px 0 0' }}>Yayın tarihine göre, yeniden eskiye.</p></section>
      {Object.entries(gruplar).map(([d, l]) => (
        <section key={d} style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <h2 style={{ fontSize: 20 }}>{trUzun(d)} <span className="mut" style={{ fontSize: 14, fontWeight: 400 }}>· {l.length} yayın</span></h2>
          {l.map((x) => <Kart key={x.id} x={x} izleme={izleme} />)}</section>))}
      {!liste.length && <Bos>Yayın bulunamadı.</Bos>}
    </main>)
}

export function Onemli({ liste, izleme }) {
  const t = bugun(), s = puanSirala(liste, t)
  return (
    <main className="w sayfa"><section><h1 className="buyuk" style={{ fontSize: 34 }}>Önemli değişiklikler</h1>
      <p className="mut" style={{ margin: '8px 0 0', maxWidth: 760 }}>Tüm yayınlar puana göre sıralanır. Puan: önem seviyesi (en çok 55) + yaklaşan tarih (20) + yayının yeniliği (15) + analiz güveni (10). Puanın üzerine gelince dağılımı görürsün.</p></section>
      {s.map(({ x, p }) => <Kart key={x.id} x={x} p={p} izleme={izleme} />)}
      {!s.length && <Bos>Yayın bulunamadı.</Bos>}</main>)
}

export function Takvim({ veri }) {
  const t = bugun(), hepsi = []
  veri.yayinlar.forEach((x) => [['gorus_son_tarihi', 'Görüş son tarihi'], ['yururluk_tarihi', 'Yürürlük'], ['uyum_son_tarihi', 'Uyum']]
    .forEach(([f, n]) => { if (x[f]) hepsi.push({ d: x[f], n, x }) }))
  hepsi.sort((a, b) => a.d.localeCompare(b.d))
  const ileri = hepsi.filter((v) => v.d >= t), gecmis = hepsi.filter((v) => v.d < t).reverse()
  const grupla = (l) => { const g = {}; l.forEach((v) => (g[v.d.slice(0, 7)] ||= []).push(v)); return Object.entries(g) }
  const blok = (l, ad) => grupla(l).map(([ay, v]) => (
    <section className="card" key={ad + ay}><h2 style={{ fontSize: 20 }}>{AYUZUN[+ay.slice(5) - 1]} {ay.slice(0, 4)} <span className="mut" style={{ fontSize: 13, fontWeight: 400 }}>· {ad}</span></h2>
      {v.map((e, i) => (<a key={i} className="tarihkutu" href={'#y-' + e.x.id}>
        <div className="g"><b>{+e.d.slice(8)}</b><span>{AY[+e.d.slice(5, 7) - 1]}</span></div>
        <div style={{ minWidth: 0 }}><div className="mut" style={{ fontSize: 12 }}>{e.n} · {kn(e.x.kurum)} · <Sev o={e.x.onem} /></div><div style={{ fontWeight: 500 }}>{e.x.baslik_tr}</div></div></a>))}</section>))
  return (<main className="w sayfa"><section><h1 className="buyuk" style={{ fontSize: 34 }}>Düzenleyici takvim</h1>
    <p className="mut" style={{ margin: '8px 0 0' }}>Yürürlük, uyum ve görüş bildirme tarihleri. Yalnızca belgede yazan tarihler gösterilir.</p></section>
    {blok(ileri, 'yaklaşan')}{!ileri.length && <Bos>Yaklaşan tarih yok.</Bos>}
    {gecmis.length > 0 && <><h2 style={{ fontSize: 22 }}>Geçmiş tarihler</h2>{blok(gecmis, 'geçmiş')}</>}
  </main>)
}

export function Arsiv({ liste, veri, q }) {
  const [f, setF] = useState({ kurum: '', onem: '', statu: '', konu: '' })
  const sec = (ad) => [...new Set(veri.yayinlar.map((x) => x[ad]))].sort()
  const l = liste.filter((x) => Object.entries(f).every(([k, v]) => !v || x[k] === v)).sort((a, b) => b.yayin_tarihi.localeCompare(a.yayin_tarihi))
  const S = ({ ad, e, ks }) => (<label>{e}<select value={f[ad]} onChange={(ev) => setF({ ...f, [ad]: ev.target.value })}>
    <option value="">Tümü</option>{sec(ad).map((v) => <option key={v} value={v}>{ad === 'kurum' ? kn(v) : v}</option>)}</select></label>)
  return (<main className="w sayfa"><section><h1 className="buyuk" style={{ fontSize: 34 }}>Arşiv</h1>
    <p className="mut" style={{ margin: '8px 0 0' }}>Şimdilik yalnızca son bir ay. Veri 3, 6 ve 12 aya genişledikçe arşiv de büyüyecek.</p></section>
    <div className="filtre"><S ad="kurum" e="Kurum" /><S ad="onem" e="Önem" /><S ad="statu" e="Statü" /><S ad="konu" e="Konu" />
      <span className="mut" style={{ fontSize: 13 }}>{l.length} yayın{q ? ` · “${q}”` : ''}</span></div>
    <Tablo liste={l} puanlar={(x) => puanla(x)} /></main>)
}

export function Kurumlar({ veri, izleme }) {
  return (<main className="w sayfa"><section><h1 className="buyuk" style={{ fontSize: 34 }}>Kurumlar</h1>
    <p className="mut" style={{ margin: '8px 0 0' }}>İzlenen resmî kaynaklar. Birine tıklayınca o kaynaktan toplanan tüm haberleri görürsün.</p></section>
    {['uluslararasi', 'turkiye'].map((b) => (<section key={b}><h2 style={{ fontSize: 20, marginBottom: 12 }}>{b === 'turkiye' ? 'Türkiye' : 'Uluslararası'}</h2>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill,minmax(240px,1fr))', gap: 12 }}>
        {veri.kaynaklar.filter((s) => (s.bolge === 'turkiye') === (b === 'turkiye')).map((s) => {
          const ad = veri.adaylar.filter((a) => a.kurum === s.id), an = ad.filter((a) => a.durum === 'analiz').length
          return (<a key={s.id} href={'#kurum-' + s.id} className="card" style={{ color: 'inherit' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}><b>{s.ad}</b>{izleme.kurum.includes(s.id) && <span>★</span>}</div>
            <div className="mut" style={{ fontSize: 13, marginTop: 4 }}>{ad.length} haber · {an} analiz</div>
            <div className="mut" style={{ fontSize: 12 }}>{s.aktif ? (s.ardisik_hata ? 'Son taramada hata' : 'Erişilebilir') : 'İlk sürümde kapsam dışı'}</div></a>)
        })}</div></section>))}</main>)
}

const DURUM = { analiz: 'Analiz edildi', ilgisiz: 'İlgisiz bulundu', elendi: 'Anahtar kelime süzgecinde elendi', bekliyor: 'Analiz bekliyor' }
export function Kurum({ id, veri, izleme }) {
  const s = veri.kaynaklar.find((k) => k.id === id)
  const ad = veri.adaylar.filter((a) => a.kurum === id).sort((a, b) => (b.tarih || '').localeCompare(a.tarih || ''))
  const yay = Object.fromEntries(veri.yayinlar.map((x) => [x.id, x]))
  if (!s && !ad.length) return <main className="w sayfa">Kaynak bulunamadı. <a href="#kurumlar">Kurumlar</a></main>
  return (<main className="w sayfa"><section><div className="mut" style={{ fontSize: 13 }}><a href="#kurumlar">Kurumlar</a> / {kn(id)}</div>
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12, alignItems: 'center', justifyContent: 'space-between', marginTop: 6 }}>
      <h1 className="buyuk" style={{ fontSize: 34 }}>{s ? s.ad : kn(id)}</h1>
      <button className={'yildiz' + (izleme.kurum.includes(id) ? ' on' : '')} onClick={() => izleme.degistir('kurum', id)}>{izleme.kurum.includes(id) ? '★ İzleniyor' : '☆ Kurumu izle'}</button></div>
    <p className="mut" style={{ margin: '8px 0 0' }}>Bu kaynaktan toplanan {ad.length} haber. Süzgeçte elenenler de burada, nedeniyle birlikte listelenir.</p></section>
    <div className="card tablo"><table style={{ minWidth: 700 }}><thead><tr><th>Tarih</th><th>Başlık</th><th>Durum</th><th>Önem</th></tr></thead><tbody>
      {ad.map((a) => { const y = yay[a.id]; return (<tr key={a.id + a.url}>
        <td className="mut" style={{ whiteSpace: 'nowrap' }}>{a.tarih ? trKisa(a.tarih) : '—'}</td>
        <td>{y ? <a href={'#y-' + y.id}>{y.baslik_tr}</a> : <a href={a.url} target="_blank" rel="noopener noreferrer">{a.baslik} ↗</a>}</td>
        <td style={{ fontSize: 12 }}>{DURUM[a.durum]}{a.durum === 'elendi' && a.neden ? ` (${a.neden})` : ''}</td>
        <td>{y ? <Sev o={y.onem} /> : '—'}</td></tr>) })}</tbody></table></div></main>)
}

export function Izleme({ veri, izleme }) {
  const yl = veri.yayinlar.filter((x) => izleme.yayin.includes(x.id))
  return (<main className="w sayfa"><section><h1 className="buyuk" style={{ fontSize: 34 }}>İzleme listem</h1>
    <p className="mut" style={{ margin: '8px 0 0' }}>Liste bu tarayıcıda saklanır; başka cihazla paylaşılmaz.</p></section>
    <section><h2 style={{ fontSize: 20, marginBottom: 12 }}>Kurumlar</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>{izleme.kurum.map((k) => <a key={k} className="kaynak" href={'#kurum-' + k}>{kn(k)}</a>)}
        {!izleme.kurum.length && <span className="mut">Henüz kurum eklenmedi. Kurum sayfasındaki “Kurumu izle” düğmesini kullan.</span>}</div></section>
    <section style={{ display: 'flex', flexDirection: 'column', gap: 12 }}><h2 style={{ fontSize: 20 }}>Yayınlar</h2>
      {yl.map((x) => <Kart key={x.id} x={x} izleme={izleme} />)}
      {!yl.length && <Bos>Henüz yayın eklenmedi. Kartlardaki “İzle” düğmesini kullan.</Bos>}</section></main>)
}
