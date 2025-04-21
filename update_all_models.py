from train_models import train_and_save_model
import pandas as pd
import os

def update_model_from_csv(csv_path, model_path, column_name):
    try:
        df = pd.read_csv(csv_path)
        if column_name not in df.columns:
            raise ValueError(f"CSV faylida '{column_name}' ustuni yo'q: {csv_path}")
        data = df[column_name].tolist()
        train_and_save_model(data, model_path)
        print(f"{model_path} modeli yangilandi.")
    except Exception as e:
        print(f"Xatolik: {csv_path} — {e}")

# Model yangilash
update_model_from_csv("csv/aviator_1win.csv", "models/aviator_1win.pkl", "coefficient")
update_model_from_csv("csv/crash_1win.csv", "models/crash_1win.pkl", "coefficient")
update_model_from_csv("csv/luckyjet_1win.csv", "models/luckyjet_1win.pkl", "value")
