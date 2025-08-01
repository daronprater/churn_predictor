from setuptools import find_packages, setup

setup(
    name="churn_model",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "pydantic",
        "fastapi",
        "uvicorn",
        "joblib"
    ],
)
