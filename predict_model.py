import numpy as np
import joblib

def create_dataset(data, step=10):
    X = []
    for i in range(len(data) - step):
        X.append(data[i:i+step])
    return np.array(X)

def predict_next_value(model_path, recent_data):
    model = joblib.load(model_path)
    X = create_dataset(recent_data[-10:])
    if len(X) == 0:
        return None
    prediction = model.predict(X)
    return round(float(prediction[-1]), 
2)
