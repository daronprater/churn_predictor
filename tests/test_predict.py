from churn_model.predict import make_prediction


def test_prediction_format():
    features = {"tenure": 10, "monthly_charges": 45.0, "contract": "month-to-month"}
    pred, prob = make_prediction(features)
    assert isinstance(pred, int)
    assert isinstance(prob, float)
    assert 0.0 <= prob <= 1.0
