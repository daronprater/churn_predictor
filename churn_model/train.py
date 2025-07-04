import joblib
import pandas as pd

#from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Step 1: Simulate some data
data = pd.DataFrame({
    "tenure": [1, 12, 24, 5, 36, 60, 3, 48],
    "monthly_charges": [29.85, 56.95, 53.85, 42.30, 70.70, 89.10, 25.00, 99.25],
    "contract": ["month-to-month", "one year", "two year", "month-to-month", "two year", "two year", "month-to-month", "one year"],
    "churn": [1, 0, 0, 1, 0, 0, 1, 0]
})

# Step 2: Encode categorical variables
le = LabelEncoder()
data["contract"] = le.fit_transform(data["contract"])

# Step 3: Train/test split
X = data[["tenure", "monthly_charges", "contract"]]
y = data["churn"]

model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save the model
joblib.dump(model, "churn_model.pkl")
joblib.dump(le, "contract_encoder.pkl")