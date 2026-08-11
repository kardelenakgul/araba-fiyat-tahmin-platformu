import pandas as pd


def fetch_data():
    # Örnek veri seti: Araç verileri ve fiyatları
    url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93.csv"
    print("Veri çekiliyor...")
    df = pd.read_csv(url)

    print("\nVeri başarıyla çekildi! İşte ilk 5 satır:")
    print(df.head())

    # Çektiğimiz veriyi data klasörüne kaydedelim
    df.to_csv("cars_data.csv", index=False)
    print("\nVeri 'cars_data.csv' olarak kaydedildi.")
    return df


if __name__ == "__main__":
    fetch_data()