# churn_model/predict.py
import joblib
import numpy as np

model = joblib.load("churn_model/churn_model.pkl")
encoder = joblib.load("churn_model/contract_encoder.pkl")

def make_prediction(features: dict) -> tuple[int, float]:
    contract_encoded = encoder.transform([features['contract']])[0]
    features['contract'] = contract_encoded
    input_array = np.array([[features['tenure'], features['monthly_charges'], features['contract']]])
    pred = model.predict(input_array)[0]
    prob = model.predict_proba(input_array)[0][1]
    return int(pred), float(prob)
