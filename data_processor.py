import sqlite3
import pandas as pd


def clean_and_save_to_db():
    # 1. Çektiğimiz veriyi yüklüyoruz
    df = pd.read_csv("cars_data.csv")

    # 2. Tahmin ve analiz için işimize yarayacak temel sütunları seçiyoruz
    selected_columns = [
        "Manufacturer",
        "Model",
        "Type",
        "Price",
        "MPG.city",
        "EngineSize",
        "Horsepower",
        "Weight",
    ]
    df_cleaned = df[selected_columns].copy()

    # 3. Eksik (null) değerler varsa temizliyoruz
    df_cleaned.dropna(inplace=True)

    print("Temizlenmiş verinin ilk 5 satırı:")
    print(df_cleaned.head())

    # 4. SQLite veritabanına bağlantı oluşturup tabloya kaydediyoruz
    conn = sqlite3.connect("cars_database.db")
    df_cleaned.to_sql("cars", conn, if_exists="replace", index=False)
    conn.close()

    print("\nVeri temizlendi ve 'cars_database.db' veritabanına kaydedildi!")


if __name__ == "__main__":
    clean_and_save_to_db()