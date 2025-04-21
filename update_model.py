import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor

def create_dataset(data, step=10):
    X, y = [], []
    for i in range(len(data) - step):
        X.append(data[i:i+step])
        y.append(data[i+step])
    return np.array(X), np.array(y)

def train_model(csv_path, model_name):
    if not os.path.exists(csv_path):
        print(f"[X] {csv_path} topilmadi.")
        return

    df = pd.read_csv(csv_path)
    if 'coefficient' not in df.columns:
        print(f"[X] {csv_path} faylida 'coefficient' nomli ustun topilmadi.")
        return

    data = df['coefficient'].values
    X, y = create_dataset(data)

    model = RandomForestRegressor()
    model.fit(X, y)

    os.makedirs("ai_models", exist_ok=True)
    joblib.dump(model, f"ai_models/{model_name}.pkl")
    print(f"[✓] {model_name}.pkl modeli yangilandi!")

if __name__ == "__main__":
    print("Model .csv fayldan avtomatik yangilanmoqda...")

    # Har bir o‘yinga alohida CSV va model nomi
    model_info = {
        "aviator_1win": "csv/aviator_1win.csv",
        "aviator_mostbet": "csv/aviator_mostbet.csv",
        "luckyjet_1win": "csv/luckyjet_1win.csv",
        "crash": "csv/crash.csv",
        "mines": "csv/mines.csv",
        "dice": "csv/dice.csv",
        "hilo": "csv/hilo.csv"
    }

    for model_name, csv_path in model_info.items():
        train_model(csv_path, model_name)
