# Churn Predictor API

A FastAPI application that predicts customer churn based on input data using a trained machine learning model.

## Features

- REST API endpoint for churn prediction
- Model inference with scikit-learn
- Logging of predictions
- Automated testing with pytest
- CI pipeline with GitHub Actions

## Getting Started

### Prerequisites

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/installation/)
- Git

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create and Activate the Virtual Environment
    ```python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows PowerShell

3. Install Dependencies
    ```pip install -r requirements.txt


### Running the API

Start the fastAPI server with the below
    ```uvicorn main:app --reload

### API Usage
POST /predict

Request body (JSON):
    ```{
  "customer_id": 123,
  "tenure": 10,
  "monthly_charges": 45.0,
  "contract": "month-to-month"
    }

Response:
    ```
    {
  "churn_prediction": 0,
  "churn_probability": 0.123
    }

### Running Tests
Run test using pytest

### CI/CD
This project uses GitHub Actions to run tests automatically on every push and pull request.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request.



