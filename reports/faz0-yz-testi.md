# Faz 0 · Yapay zekâ testi (GitHub Models ve Gemini)

Denenenler: gemini:gemini-3-flash-preview

| Model | Kaynak | Sonuç | Süre (sn) | Gönderilen kr | Token (girdi/çıktı) | Teyitli alıntı birebir | Önem | Statü |
|---|---|---|---|---|---|---|---|---|
| gemini:gemini-3-flash-preview | BIS/BCBS | OK | 8.4 | 2549 | 953/686 | 0/2 | Dusuk | Nihai |
| gemini:gemini-3-flash-preview | ECB | OK | 32.5 | 40000 | 38741/456 | 1/1 | Dusuk | Bilgi amacli |
| gemini:gemini-3-flash-preview | Resmi Gazete | OK | 33.7 | 40000 | 20098/478 | 1/1 | Dusuk | Nihai |

## gemini:gemini-3-flash-preview · BIS/BCBS
Belge: Basel Committee publishes more details on the 2026 assessment of global systemically important banks — https://www.bis.org/media-releases/20261125-basel-committee-publishes-more-details-2026-assessment-global-systemically-important-banks

```json
{
  "ilgili_mi": true,
  "konu": "Basel",
  "statu": "Nihai",
  "onem": "Dusuk",
  "onem_gerekcesi": "Belge, kuresel sistemik oneme sahip bankalarin (G-SIB) degerlendirilmesine iliskin metodolojik detaylari icermektedir. Yerel bir kamu bankasinin G-SIB listesinde yer alma olasiligi dusuk oldugundan, dogrudan bir sermaye yukumlulugu dogurmamaktadir.",
  "yonetici_ozeti": "Basel Komitesi, 2026 yili G-SIB degerlendirmesine iliskin metodolojik gostergeleri, payda degerlerini ve esik puanlarini yayımlamistir. Bu calisma, Finansal Istikrar Konseyi (FSB) tarafindan guncellenen G-SIB listesiyle es zamanli olarak paylasilmistir. Degerlendirme, bankalarin 2025 mali yil sonu verilerine dayanmakta ve sistemik onem puanlarina gore ek sermaye yukumluluklerini belirlemektedir.",
  "teyitli": [
    {
      "hukum": "G-SIB puanlarini hesaplamak icin kullanilan gosterge paydalari ve banka verileri yayimlanmistir.",
      "alinti": "The publication accompanies the Financial Stability Board's release of the updated list of G-SIBs and includes: The denominators of the high-level indicators..."
    },
    {
      "hukum": "Metodoloji, bankalarin sistemik onemini bir onceki mali yil sonu verilerini kullanarak degerlendirmektedir.",
      "alinti": "The Committee's methodology assesses the systemic importance of global banks using indicators calculated from data for the previous fiscal year-end (2025)..."
    }
  ],
  "olasi_etki": [
    "Bankanin G-SIB listesinde yer almamasi durumunda dogrudan bir ek sermaye tamponu (higher loss-absorbency) etkisi beklenmemektedir.",
    "Yerel duzenleyici kurumun (BDDK) D-SIB (Yurt Ici Sistemik Onemli Bankalar) metodolojisini bu guncellemelerle uyumlu hale getirmesi durumunda raporlama surecleri etkilenebilir.",
    "Kuresel piyasalardaki sistemik risk algisinin ve bankalarin goreceli konumlarinin izlenmesi acisindan bilgi amacli kullanilabilir."
  ],
  "tarihler": [
    {
      "tur": "Yayin Tarihi",
      "tarih": "2026-11-25"
    },
    {
      "tur": "Veri Referans Tarihi",
      "tarih": "2025-12-31"
    }
  ],
  "etkilenen_alanlar": [
    "Raporlama",
    "RWA"
  ]
}
```

## gemini:gemini-3-flash-preview · ECB
Belge: Introduction to the ECB Token Reference Model - a framework for standardisation discussions — https://www.ecb.europa.eu//pub/pdf/other/ecb.introproposalTRM2026.en.pdf

```json
{
  "ilgili_mi": true,
  "konu": "Diger",
  "statu": "Bilgi amacli",
  "onem": "Dusuk",
  "onem_gerekcesi": "Belge, yasal bir zorunluluk veya sermaye yeterliligi hesaplamasini etkileyen bir kural getirmemektedir. Yalnizca dijital varlik ekosistemi icin kavramsal bir referans modeli sunmaktadir.",
  "yonetici_ozeti": "Avrupa Merkez Bankasi (ECB) tarafindan sunulan bu belge, tokenizasyon ekosistemi icin ortak bir terminoloji ve teknik referans modeli olusturmayi amaclamaktadir. Belge, farkli platformlar arasindaki birlikte calisabilirligi artirmak icin bir tartisma cercevesi sunar. Mevcut bankacilik operasyonlari veya risk yonetimi modelleri uzerinde dogrudan bir yukumluluk yaratmamaktadir.",
  "teyitli": [
    {
      "hukum": "Belge, standardizasyon tartismalari icin bir cerceve sunan referans modelidir.",
      "alinti": "Introduction to the ECB Token Reference Model - a framework for standardisation discussions"
    }
  ],
  "olasi_etki": [
    "Gelecekteki dijital varlik ve saklama hizmetleri altyapisinin bu modele gore tasarlanmasi",
    "Dijital varlik ekosistemine yonelik stratejik teknoloji planlamasi",
    "Sektorel standartlasma tartismalarina uyum saglanmasi"
  ],
  "tarihler": [
    {
      "tur": "Yayin Tarihi",
      "tarih": "belirtilmemis"
    }
  ],
  "etkilenen_alanlar": [
    "Diger (Dijital Varlik Altyapisi)",
    "Raporlama"
  ]
}
```

## gemini:gemini-3-flash-preview · Resmi Gazete
Belge: Resmi Gazete - gunun icindekiler — https://www.resmigazete.gov.tr/

```json
{
  "ilgili_mi": true,
  "konu": "Diger",
  "statu": "Nihai",
  "onem": "Dusuk",
  "onem_gerekcesi": "Belge iceriginde bankacilik sektorunu, Basel standartlarini veya TFRS 9 uygulamalarini dogrudan etkileyen yeni bir duzenleme bulunmamaktadir. Sadece rutin operasyonel veri paylasimi mevcuttur.",
  "yonetici_ozeti": "26 Kasim 2026 tarihli Resmi Gazete'nin icindekiler bolumunu iceren belgede, universite yonetmeliklerinin iptali, ithalatta haksiz rekabetin onlenmesine dair bir teblig ve cesitli yargi kararlari yer almaktadir. Bankacilik faaliyetlerini dogrudan ilgilendiren tek madde, Merkez Bankasi'nin gunluk doviz kurlari ve borclanma senetleri degerlerini duyurmasidir. Kamu bankasinin risk yonetimi veya raporlama standartlarinda bir degisiklik yaratmamaktadir.",
  "teyitli": [
    {
      "hukum": "Merkez Bankasi gunluk verilerinin yayimi",
      "alinti": "T.C. Merkez Bankasınca Belirlenen Döviz Kurları ve Devlet İç Borçlanma Senetlerinin Günlük Değerleri"
    }
  ],
  "olasi_etki": [
    "Gunluk doviz kuru ve DIBS degerlemeleri uzerinden rutin muhasebe ve raporlama surecleri devam edecektir.",
    "Bankanin Basel standart yaklasimi veya TFRS 9 karsilik hesaplama yontemleri uzerinde herhangi bir etkisi bulunmamaktadir."
  ],
  "tarihler": [
    {
      "tur": "Yayin Tarihi",
      "tarih": "2026-11-26"
    }
  ],
  "etkilenen_alanlar": [
    "Raporlama"
  ]
}
```
