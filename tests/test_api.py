from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_predict_churn():
    payload = {
        "customer_id": 123,
        "tenure": 10,
        "monthly_charges": 45.0,
        "contract": "month-to-month"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "churn_prediction" in data
    assert "churn_probability" in data
    assert isinstance(data["churn_prediction"], int)

def test_predict_missing_field():
    payload = {
        "customer_id": 123,
        # "tenure" is missing
        "monthly_charges": 45.0,
        "contract": "month-to-month"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_predict_invalid_type():
    payload = {
        "customer_id": "abc",  # should be int
        "tenure": "ten",       # should be int
        "monthly_charges": "free",  # should be float
        "contract": 123        # should be str
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 422


