// Yerel/tek dosyalik onizleme: veri sayfaya gomulu, ag istegi yok.
import { createRoot } from 'react-dom/client'
import { useEffect, useState } from 'react'
import './src/stil.css'
import { Uygulama } from './src/App.jsx'
import yayinlar from './public/data/yayinlar.json'
import adaylar from './public/data/adaylar.json'
import kaynaklar from './public/data/kaynaklar.json'
const veri = { yayinlar, adaylar, kaynaklar }
function Kok() {
  const [rota, setRota] = useState(location.hash.slice(1) || 'ana'), [q, setQ] = useState('')
  const [iz, setIz] = useState({ yayin: [], kurum: [] })
  useEffect(() => { const h = () => { const r = location.hash.slice(1) || 'ana'; if (/^s\d+$/.test(r)) return; setRota(r); window.scrollTo(0, 0) }
    window.addEventListener('hashchange', h); return () => window.removeEventListener('hashchange', h) }, [])
  const degistir = (t, id) => setIz((o) => ({ ...o, [t]: o[t].includes(id) ? o[t].filter((v) => v !== id) : [...o[t], id] }))
  return <Uygulama veri={veri} rota={rota} izleme={{ ...iz, degistir }} q={q} setQ={setQ} />
}
createRoot(document.getElementById('root')).render(<Kok />)
