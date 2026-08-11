import sqlite3
import joblib
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import streamlit as st

# Sayfa Başlığı ve Düzeni
st.set_page_config(page_title="Araba Fiyat Tahmin Platformu", layout="wide")
st.title("🚗 Araba Fiyat Tahmin ve Analiz Platformu")
st.write(
    "Girdiğiniz araç özelliklerine göre makine öğrenmesi modeli ile tahmini fiyat hesaplayın."
)

# 1. Kaydedilmiş Modeli Yüklüyoruz
model = joblib.load("price_model.pkl")

# 2. Kullanıcı Girdileri (Sol Yan Menü)
st.sidebar.header("🛠️ Araç Özelliklerini Girin")

engine_size = st.sidebar.slider(
    "Motor Hacmi (Engine Size - L)", 1.0, 6.0, 2.5, 0.1
)
horsepower = st.sidebar.number_input(
    "Beygir Gücü (Horsepower)",
    min_value=50,
    max_value=500,
    value=150,
    step=5,
)
weight = st.sidebar.number_input(
    "Araç Ağırlığı (Weight - lbs)",
    min_value=1500,
    max_value=6000,
    value=3000,
    step=50,
)
mpg_city = st.sidebar.slider(
    "Şehir İçi Yakıt Tüketimi (MPG City)", 10, 50, 25, 1
)

# 3. Tahmin Butonu ve Hesaplama
if st.sidebar.button("Fiyatı Tahmin Et"):
    # Model girdisini hazırlama (const sabit terimini ekleyerek)
    input_data = pd.DataFrame(
        {
            "const": [1.0],
            "EngineSize": [engine_size],
            "Horsepower": [horsepower],
            "Weight": [weight],
            "MPG.city": [mpg_city],
        }
    )

    prediction = model.predict(input_data)[0]

    # Tahmin sonucunu gösterme
    st.success(f"### 💡 Tahmini Araç Fiyatı: **${prediction * 1000:,.2f}**")

# 4. Veritabanından Veri Görselleştirme (Grafikler)
st.subheader("📊 Veritabanı Analiz Paneli")

conn = sqlite3.connect("cars_database.db")
df = pd.read_sql_query("SELECT * FROM cars", conn)
conn.close()

col1, col2 = st.columns(2)

with col1:
    st.write("#### Beygir Gücü - Fiyat İlişkisi")
    fig1 = px.scatter(
        df,
        x="Horsepower",
        y="Price",
        color="Type",
        hover_data=["Manufacturer", "Model"],
        title="Beygir Gücü arttıkça Fiyat Değişimi",
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("#### Araç Tiplerine Göre Ortalama Fiyat")
    fig2 = px.bar(
        df.groupby("Type")["Price"].mean().reset_index(),
        x="Type",
        y="Price",
        color="Type",
        title="Araç Kasa Tipleri Fiyat Dağılımı",
    )
    st.plotly_chart(fig2, use_container_width=True)