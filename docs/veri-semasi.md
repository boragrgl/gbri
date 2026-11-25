# GBRI · Veri Şeması

Onay: 26 Kasım 2026 · Faz 0 sonunda kabul edildi. Kaynak belge: https://claude.ai/artifact/SVNutZnHi2HcXFpzT6RFUM

## Amaç ve temel ilkeler

GBRI'nin tüm verisi GitHub reposunda JSON dosyaları olarak tutulur; veritabanı yok. Günlük tarama bu dosyaları günceller, site (Cloudflare Pages) yalnızca okur.

- **Yayın tarihi ile tespit tarihi ayrıdır.** Bir belge sisteme ilk kez girdi diye "yeni değişiklik" sayılmaz; sıralama ve "yeni" işareti kurumun yayın tarihine göre yapılır.
- **İlk yükleme başlangıç arşividir.** Son 12 ayın belgeleri `baslangic_arsivi: true` ile işaretlenir ve bildirim üretmez.
- **Teyitli hüküm ile yapay zekâ yorumu ayrı alanlardadır.** Teyitli her hüküm belgeden birebir alıntı ve sayfa/paragraf referansı taşır; alıntı otomatik kontrol edilir.
- **Orijinal belge kopyalanmaz.** Bağlantısı, içerik özeti (hash) ve analiz için çıkarılan metin saklanır.
- **Önem, banka profiline göre verilir:** standart yaklaşım kullanan, TFRS 9 uygulayan kamu bankası.
- **Alan adları Türkçe ve ASCII'dir** (`yayin_tarihi`, `onem`); ekranda görünen değerler Türkçe karakterlidir (`Yüksek`, `İstişare`).

## Dosya yapısı

```
data/
  yayinlar/
    2026-11.json        # o ay yayımlanan tüm kayıtlar (tam analiz dahil)
    2026-10.json
    …
  metin/
    <kayit_id>.txt.gz   # analize giren çıkarılmış metin (alıntı kontrolü için)
  indeks/
    genel-bakis.json    # günün özeti, KPI'lar, önemli değişiklikler (üst 20)
    liste.json          # tüm kayıtların kısa hali: filtre ve arama için
    takvim.json         # yaklaşan ve geçmiş tüm son tarihler
    konular.json        # konu ve alt konu sayıları, parametre etki haritası
  kaynaklar.json        # kaynak listesi + son tarama durumu
  tarama-gunlugu.json   # son 30 taramanın özeti
config/
  sources.json          # izlenen adresler (elle düzenlenir)
  profil.json           # banka profili ve önem kuralları
schema/
  yayin.schema.json     # yayın kaydının doğrulama şeması
```

## Yayın kaydı

| Alan | Tür | Zorunlu | Açıklama | Ekranda nerede |
| --- | --- | --- | --- | --- |
| `id` | metin | evet | `bddk-2026-11-23-a1b2c3`: kurum + yayın tarihi + adres hash'inin ilk 6 hanesi | Detay sayfası adresi |
| `kurum` | metin | evet | Kaynak kimliği (`bddk`, `bcbs`, `eba` …) | Kartlar, Kurumlar filtresi |
| `baslik_orijinal` | metin | evet | Belgenin kendi dilindeki başlığı | Detay sayfası |
| `baslik_tr` | metin | evet | Türkçe başlık | Kartlar, tablo |
| `url` | metin | evet | Orijinal belgenin resmî adresi | "Orijinal belge" düğmesi |
| `belge_turu` | sabit liste | evet | Yönetmelik, rehber, istişare dokümanı … | Tablo "Tür" sütunu |
| `statu` | sabit liste | evet | Taslak / İstişare / Nihai / Yürürlükte / Bilgi amaçlı | Statü çipi ve adım çizgisi |
| `onem` | sabit liste | evet | Kritik / Yüksek / Orta / Düşük | Renkli işaret, sıralama |
| `onem_gerekcesi` | metin | evet | Önemin banka profiline göre kısa gerekçesi | Detay sayfası |
| `konu` | sabit liste | evet | TFRS 9 / Basel / Sürdürülebilirlik / Risk Yönetimi / Diğer | Konu sayfaları |
| `alt_konular` | liste | hayır | ECL, PD, LGD, SICR, RWA … | Alt konu çipleri, etki haritası |
| `etkilenen_alanlar` | liste | hayır | Kartlardaki "Etkilenen" etiketleri | Kartlar |
| `ozet_tek_satir` | metin | evet | Kart için 1–2 cümlelik Türkçe özet | Kartlar |
| `yayin_tarihi` | tarih | evet | Kurumun belgeyi yayımladığı gün | Sıralama, "son 24 saat" |
| `tespit_zamani` | tarih-saat | evet | Taramanın belgeyi ilk gördüğü an | Detay sayfası |
| `gorus_son_tarihi` | tarih | hayır | İstişare için görüş verme son günü | Takvim |
| `yururluk_tarihi` | tarih | hayır | Belgede yazıyorsa; yoksa boş ve "belirtilmemiş" | Detay sayfası, takvim |
| `uyum_son_tarihi` | tarih | hayır | Uygulama ya da raporlama başlangıcı | Takvim |
| `baslangic_arsivi` | evet/hayır | evet | İlk 12 aylık yüklemeden gelen kayıt | "Yeni" işareti verilmez |
| `ilgili_mi` | evet/hayır | evet | Bankacılıkla ilgisiz belgeler listelerde gizlenir, arşivde kalır | Filtre |
| `analiz` | nesne | ilgiliyse | 12 bölümlük analiz | Detay sayfası |
| `analiz_bilgisi` | nesne | ilgiliyse | Model, zaman, alıntı doğrulama, güven | "Analiz bilgisi" kartı |
| `surumler` | liste | evet | Sürüm geçmişi | "Sürüm geçmişi" kartı |
| `onceki_kayit`, `sonraki_kayit` | metin | hayır | İstişare → nihai zinciri | Statü çizgisi |
| `ilgili_kayitlar` | liste | hayır | Aynı konudaki diğer kayıtların `id`'leri | "İlgili yayınlar" kartı |

## Analiz alanları

`analiz` nesnesi 12 bölümü karşılar. Bölümlerin çoğu iki listeden oluşur: `teyitli` (belgede yazan) ve `olasi_etki` (yapay zekâ yorumu).

| # | Bölüm | Alan | İçerik |
| --- | --- | --- | --- |
| 1 | Yönetici özeti | `yonetici_ozeti` | 3–4 cümle, düz metin |
| 2 | Yayının amacı | `amac` | teyitli + olası etki |
| 3 | Önceki düzenleyici çerçeve | `onceki_cerceve` | teyitli + olası etki; `karsilastirma_kaynagi`: `arsiv` ya da `genel_bilgi` (doğrulanmamış) |
| 4 | Yeni hükümler ve değişiklikler | `degisiklikler` | Liste: `konu`, `onceki`, `yeni`, `referans` |
| 5 | Teknik etkiler | `teknik_etkiler` | teyitli + olası etki |
| 6 | Bankacılık operasyonlarına etki | `operasyonel_etki` | teyitli + olası etki |
| 7 | PD, LGD, EAD, ECL | `parametre_etkisi` | Her parametre için `duzey` + `not` |
| 8 | Sermaye ve RWA | `sermaye_rwa` | teyitli + olası etki |
| 9 | İklim ve sürdürülebilirlik | `iklim` | teyitli + olası etki; ilgili değilse `ilgili_degil: true` |
| 10 | Tarihler | `tarihler` | Liste: `tur`, `tarih`, `referans` |
| 11 | Gözden geçirilecek alanlar | `gozden_gecirilecekler` | Liste: `baslik`, `aciklama`; tümü olası etki niteliğindedir |
| 12 | Kaynak ve referanslar | `referanslar` | Liste: `metin`, `sayfa`, `paragraf` |

**Teyitli bir hükmün yapısı:** `hukum`, `alinti` (belgeden birebir, kısaltmasız, en fazla 25 kelime), `sayfa`, `paragraf`, `alinti_dogrulandi`. Doğrulanamayan alıntı teyitli listesinden çıkarılır ve olası etkiye taşınır.

**Analiz bilgisi** (`analiz_bilgisi`): `model`, `olusturma_zamani`, `gonderilen_karakter`, `alinti_dogrulanan`, `alinti_toplam`, `guven`.

## Sabit listeler

| Liste | Değerler |
| --- | --- |
| Önem | Kritik, Yüksek, Orta, Düşük |
| Statü | Taslak, İstişare, Nihai, Yürürlükte, Bilgi amaçlı |
| Belge türü | Kanun, Yönetmelik, Tebliğ, Genelge, Rehber, Standart, İstişare dokümanı, Rapor, Basın duyurusu, Bülten, Konuşma |
| Konu | TFRS 9, Basel, Sürdürülebilirlik, Risk Yönetimi, Diğer |
| TFRS 9 alt konuları | ECL, PD, LGD, EAD, SICR, Aşama 1-2-3, Temerrüt tanımı, Değer düşüklüğü, Kalibrasyon ve validasyon |
| Basel alt konuları | Kredi riski, Standart yaklaşım, İRD, RWA, Sermaye yeterliliği, Operasyonel risk, Likidite riski |
| Sürdürülebilirlik alt konuları | ESG, Fiziksel risk, Geçiş riski, IFRS S1/S2, TSRS, CSRD, İklim stres testi, Teminat değerlemesi |
| Risk Yönetimi alt konuları | Kredi sınıflandırma, Karşılıklar, Raporlama, Model riski, Stres testi, Makro ihtiyati, Finansal istikrar |
| Etki düzeyi | Yüksek, Orta, Düşük, Dolaylı, Etki beklenmiyor, İlgili değil |
| Güven | Yüksek, Orta, Düşük |

**Önem kuralları** (`config/profil.json`): bankayı doğrudan bağlayan Türk düzenlemeleri (BDDK, TCMB, KGK, Resmî Gazete) en az Orta başlar; yalnızca İRD bankalarını ilgilendiren hükümler en fazla Düşük olur; yürürlük tarihi 90 günden yakın olan Yüksek ya da Kritik bir kayıt öne çıkar.

## Kaynak kaydı ve kaynak durumu

`data/kaynaklar.json`: `id`, `ad`, `bolge`, `yontem` (`rss` / `sayfa` / `api`), `adresler`, `aktif` (OECD ilk sürümde `false`), `son_basarili_tarama`, `ardisik_hata`, `son_hata`, `son_taramada_bulunan`.

## Sürüm ve güncelleme takibi

1. **Tanıma:** Normalleştirilmiş adres ile kurum kaydın kimliğidir; adres değişse bile aynı başlık + yayın tarihi eşleşirse aynı kayıt sayılır.
2. **Değişiklik:** `icerik_hash` değişirse yeni sürüm eklenir, kayıt "güncellendi" diye işaretlenir ve analiz yeniden yapılır.
3. **Statü ilerlemesi:** İstişarenin nihai hali ayrı belgeyse yeni kayıt açılır, iki kayıt `onceki_kayit` / `sonraki_kayit` ile bağlanır.
4. **Tekrar yok:** "Yeni" ve "güncellendi" işaretleri kayıt ve sürüm kimliğine bağlıdır.

`surumler` elemanı: `no`, `tespit_zamani`, `icerik_hash`, `degisiklik_notu`.

## Takvim ve site indeksleri

| Dosya | İçerik | Beslediği ekran |
| --- | --- | --- |
| `genel-bakis.json` | Günün özeti, 4 KPI, önem sıralı ilk 20 kayıt, konu dağılımı | Genel Bakış, Mobil |
| `liste.json` | Her kaydın kısa hali | Günlük Yayınlar, Önemli Değişiklikler, konu sayfaları, Arşiv, arama |
| `takvim.json` | `tarih`, `tur`, `kayit_id`, kurum, kısa başlık | Yaklaşan son tarihler, Takvim |
| `konular.json` | Konu/alt konu sayıları, parametre × önem matrisi | Konu sayfaları |

İzleme listesi ve "son ziyaretten beri yeni" işareti tarayıcıda tutulur.

## Onaylanan kararlar

- [x] Veriler aya göre bölünmüş JSON dosyalarında, repoda tutulur; orijinal PDF'ler kopyalanmaz.
- [x] Son 12 ay başlangıç arşivi olarak yüklenir, "yeni" diye işaretlenmez.
- [x] Doğrulanamayan alıntı "teyitli"den çıkarılıp "olası etki"ye taşınır.
- [x] Bankacılıkla ilgisiz belgeler listelerde gizlenir, arşivde kalır.
- [x] İzleme listesi tarayıcıda tutulur.
- [x] OECD ilk sürümde kapalı kalır.
- [x] Önem kuralları bu haliyle başlar; ilk haftaların sonuçlarına göre ayarlanır.
