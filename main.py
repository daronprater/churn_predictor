from io import StringIO

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from churn_model.logger import log_prediction_to_db

app = FastAPI()

# Load model and encoder
model = joblib.load("churn_model/churn_model.pkl")
encoder = joblib.load("churn_model/contract_encoder.pkl")

# Define the Customer model for request validation
class Customer(BaseModel):
    customer_id: int = Field(..., example=123)
    tenure: int = Field(..., ge=0, example=12)
    monthly_charges: float = Field(..., ge=0.0, example=29.95)
    contract: str = Field(..., example="month-to-month")



@app.post("/batch_predict")
async def batch_predict(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode("utf-8")))

    if df.empty:
        raise HTTPException(status_code=400, detail="Uploaded CSV is empty.")

    results = []
    for _, row in df.iterrows():
        # Create a Customer object from the row
        customer = Customer(
            customer_id=row["customer_id"],
            tenure=row["tenure"],
            monthly_charges=row["monthly_charges"],
            contract=row["contract"]
        )
        # Encode the contract string using your encoder
        contract_encoded = encoder.transform([customer.contract])[0]

        # Build input_data with encoded contract instead of raw string
        input_data = pd.DataFrame([{
            "tenure": customer.tenure,
            "monthly_charges": customer.monthly_charges,
            "contract": contract_encoded
        }])
        
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0].max()
        
        log_prediction_to_db(row["customer_id"], prediction, probability)

        results.append({
            "customerID": int(row["customer_id"]),
            "prediction": int(prediction),
            "probability": round(float(probability), 3)
        })

    return {"predictions": results}


@app.post("/predict")
def predict_churn(customer: Customer):
    # This encodes the contract type using the loaded encoder
    contract_encoded = encoder.transform([customer.contract])[0]

    # This creates a X dataframe-like structure for prediction
    X = np.array([[customer.tenure, customer.monthly_charges, contract_encoded]])

    # Get prediction and probability
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]  # Probability of class 1 (churn)

    # Log it!
    log_prediction_to_db(customer.customer_id, prediction, probability)
    
    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 3)
    }
