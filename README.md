# 🚗 Uçtan Uca Araç Fiyat Tahmin ve Analiz Platformu

Bu proje, web/API üzerinden araç verilerinin çekilmesi, temizlenmesi, SQLite veritabanına aktarılması, Makine Öğrenmesi (ML) modeli ile eğitilmesi ve **Streamlit** üzerinden interaktif bir web paneli olarak sunulmasını kapsayan **uçtan uca bir veri bilimi boru hattıdır (Data Pipeline)**.

---

## 🌟 Öne Çıkan Özellikler

- **📥 Veri Toplama (`scraper.py`):** Canlı/Açık kaynak araç verilerini otomatik olarak çeker ve yerel depolamaya kaydeder.
- **🧹 Veri Ön İşleme & SQL (`data_processor.py`):** Gürültülü ve eksik verileri temizler, kritik öznitelikleri seçer ve verileri ilişkisel **SQLite** veritabanına (`cars_database.db`) kaydeder.
- **🤖 Makine Öğrenmesi Modeli (`model.py`):** Veritabanındaki verileri kullanarak araç özelliklerine (motor hacmi, beygir gücü, ağırlık vb.) göre fiyat tahmini yapan **OLS / Lineer Regresyon** modelini eğitir ve `price_model.pkl` olarak saklar.
- **📊 İnteraktif Web Arayüzü (`app.py`):** Kullanıcıların dinamik girdilerle anlık fiyat tahmini almasını ve **Plotly** grafik sistemi ile veritabanındaki trendleri analiz etmesini sağlar.

---

## 🛠️ Kullanılan Teknolojiler

- **Dil:** Python 3.13
- **Veri İşleme & Analiz:** Pandas, NumPy
- **Veritabanı:** SQLite3
- **Makine Öğrenmesi / İstatistik:** Statsmodels, Scikit-Learn
- **Görselleştirme & Web Arayüzü:** Streamlit, Plotly
- **Model Paketleme:** Joblib

---

## 📁 Proje Klasör Yapısı

```text
fiyat_tahmin_projesi/
│
├── scraper.py           # Web/API üzerinden veriyi çeken modül
├── data_processor.py    # Veriyi temizleyip SQLite veritabanına yazan modül
├── model.py             # Veriyle ML modelini eğiten ve kaydeden modül
├── app.py               # Streamlit web dashboard ve görselleştirme uygulaması
│
├── cars_data.csv        # Ham veri dosyası
├── cars_database.db     # Temizlenmiş verilerin tutulduğu SQLite veritabanı
├── price_model.pkl      # Eğitilmiş ve paketlenmiş ML modeli
│
├── requirements.txt     # Gerekli Python kütüphaneleri listesi
└── .gitignore           # Git tarafından izlenmeyecek dosyalar