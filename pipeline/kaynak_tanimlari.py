"""Izlenen kaynaklar ve okuma yontemleri (Faz 0 testlerine gore)."""

RG_KELIMELER = [
    r"bankac", r"\bbanka", r"BDDK", r"Bankacılık Düzenleme", r"Merkez Bankas", r"Kamu Gözetimi", r"KGK",
    r"Sermaye Piyasas", r"finansal", r"kredi", r"faiz", r"sürdürülebilirlik", r"muhasebe standart",
    r"TFRS", r"TMS", r"karşılık", r"özkaynak", r"sermaye yeterlili", r"likidite", r"ödeme hizmet",
    r"elektronik para", r"kripto", r"varlık yönetim", r"faktoring", r"finansal kiralama", r"tasarruf finansman",
]

KAYNAKLAR = [
    {"id": "ecb", "ad": "ECB", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "rss", "url": "https://www.ecb.europa.eu/rss/press.html", "kategori": "Basın"},
        {"tip": "rss", "url": "https://www.ecb.europa.eu/rss/pub.html", "kategori": "Yayın"},
        {"tip": "rss", "url": "https://www.bankingsupervision.europa.eu/rss/press.html", "kategori": "Bankacılık Denetimi"},
    ]},
    {"id": "fsb", "ad": "FSB", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "rss", "url": "https://www.fsb.org/feed/", "sayfa_param": "paged", "max_sayfa": 12},
    ]},
    {"id": "bis", "ad": "BIS", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "rss", "url": "https://www.bis.org/doclist/all_pressrels.rss", "kategori": "Basın"},
    ]},
    {"id": "bcbs", "ad": "BCBS", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "liste", "url": "https://www.bis.org/committees/bcbs/publications", "sayfa_sablonu": "?page={s}",
         "max_sayfa": 6, "href_desen": r"bis\.org/publications/(?!research|authors|aer|qr|bulletin|bis-paper|working-paper|central-bank)[^?#]+$",
         "tarih_once": 900, "tarih_sonra": 400, "kategori": "Yayın"},
        {"tip": "liste", "url": "https://www.bis.org/committees/bcbs/news", "sayfa_sablonu": "?page={s}",
         "max_sayfa": 4, "href_desen": r"bis\.org/media-releases/\d{8}-", "tarih_once": 900, "tarih_sonra": 400,
         "kategori": "Basın"},
    ]},
    {"id": "eba", "ad": "EBA", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "liste", "url": "https://www.eba.europa.eu/publications-and-media/press-releases",
         "sayfa_sablonu": "?page={s}", "max_sayfa": 8, "href_desen": r"/publications-and-media/press-releases/[a-z0-9-]+$",
         "tarih_once": 600, "tarih_sonra": 0, "kategori": "Basın"},
    ]},
    {"id": "ifrs", "ad": "IFRS Vakfı", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "site_haritasi", "url": "https://www.ifrs.org/sitemap.xml",
         "href_desen": r"/news-and-events/news/(?P<y>20\d\d)/(?P<m>\d\d)/[^/]+/?$", "kategori": "Haber"},
    ]},
    {"id": "issb", "ad": "ISSB", "bolge": "uluslararasi", "not": "IFRS haber beslemesinden ISSB ile ilgili olanlar ayrilir",
     "okuyucular": []},
    {"id": "worldbank", "ad": "Dünya Bankası", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "dunya_bankasi", "sorgular": ["banking regulation", "banking supervision", "climate risk financial sector"], "satir": 25},
    ]},
    {"id": "bddk", "ad": "BDDK", "bolge": "tr", "okuyucular": [
        {"tip": "liste", "url": "https://www.bddk.org.tr/Duyuru/Liste/40", "href_desen": r"/Duyuru/Detay/\d+",
         "tarih_once": 0, "tarih_sonra": 600, "kategori": "Mevzuat Duyuruları"},
        {"tip": "liste", "url": "https://www.bddk.org.tr/Duyuru/Liste/39", "href_desen": r"/Duyuru/Detay/\d+",
         "tarih_once": 0, "tarih_sonra": 600, "kategori": "Basın Duyuruları"},
        {"tip": "liste", "url": "https://www.bddk.org.tr/Duyuru/Liste/197", "href_desen": r"/Duyuru/Detay/\d+",
         "tarih_once": 0, "tarih_sonra": 600, "kategori": "Güncel Duyurular"},
        {"tip": "bddk_mevzuat", "listeler": [50, 58, 52, 54], "referans_listeler": [55, 56]},
    ]},
    {"id": "tcmb", "ad": "TCMB", "bolge": "tr", "okuyucular": [
        {"tip": "rss_kesif", "url": "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Bottom+Menu/Diger/RSS/Basin+Duyurulari",
         "kategori": "Basın Duyuruları"},
    ]},
    {"id": "kgk", "ad": "KGK", "bolge": "tr", "okuyucular": [
        {"tip": "tarihsiz_pdf_listesi", "url": "https://www.kgk.gov.tr/",
         "href_desen": r"/Portalv2Uploads/files/Duyurular/v2/(?!BankaHesap).+\.pdf", "kategori": "Duyuru"},
    ]},
    {"id": "spk", "ad": "SPK", "bolge": "tr", "okuyucular": [
        {"tip": "liste", "url": "https://spk.gov.tr/duyurular/basin-duyurulari/2026",
         "href_desen": r"/duyurular/basin-duyurulari/20\d\d/[a-z0-9-]+$", "tarih_once": 0, "tarih_sonra": 300,
         "kategori": "Basın Duyuruları"},
    ]},
    {"id": "resmigazete", "ad": "Resmî Gazete", "bolge": "tr", "okuyucular": [
        {"tip": "resmi_gazete", "anahtar_kelimeler": RG_KELIMELER},
    ]},
    {"id": "imf", "ad": "IMF", "bolge": "uluslararasi", "okuyucular": [
        {"tip": "imf_koleksiyon", "adresler": [
            ("https://www.imf.org/en/publications/gfsr/index.json", "Global Financial Stability Report"),
            ("https://www.imf.org/en/publications/weo/index.json", "World Economic Outlook"),
            ("https://www.imf.org/en/publications/fm/index.json", "Fiscal Monitor"),
            ("https://www.imf.org/en/blogs/index.json", "IMF Blog")]},
    ]},
    {"id": "oecd", "ad": "OECD", "bolge": "uluslararasi", "aktif": False,
     "not": "Site otomatik erisimi engelliyor (Faz 0 testi)", "okuyucular": []},
]
