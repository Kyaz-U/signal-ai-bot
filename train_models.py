import numpy as np from sklearn.ensemble import RandomForestRegressor import joblib

def create_dataset(data, step=10): X, y = [], [] for i in range(len(data) - step): X.append(data[i:i+step]) y.append(data[i+step]) return np.array(X), np.array(y)

def train_and_save_model(data, model_name): X, y = create_dataset(data) model = RandomForestRegressor() model.fit(X, y) joblib.dump(model, f"models/{model_name}.pkl") print(f"Model {model_name} saqlandi.")
