import sqlite3
import pandas as pd
import statsmodels.api as sm
import joblib

def train_model():
    # 1. SQL Veritabanından veriyi çekiyoruz
    conn = sqlite3.connect("cars_database.db")
    df = pd.read_sql_query("SELECT * FROM cars", conn)
    conn.close()

    # 2. Girdi (X) ve Hedef Değişkeni (y) belirliyoruz
    X = df[['EngineSize', 'Horsepower', 'Weight', 'MPG.city']]
    y = df['Price']

    # Sabit terim (intercept) ekliyoruz
    X_with_const = sm.add_constant(X)

    # 3. Modeli oluşturup eğitiyoruz
    model = sm.OLS(y, X_with_const).fit()

    print("Model Başarıyla Eğitildi!")
    print(model.summary())

    # 4. Modeli kaydediyoruz
    joblib.dump(model, "price_model.pkl")
    print("\nModel 'price_model.pkl' olarak kaydedildi!")

if __name__ == "__main__":
    train_model()