from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Load the model
try:
    model = joblib.load("best_random_forest_model.pkl")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the House Price Prediction API!",
        "instructions": "Go to /docs for API documentation, or use /predict to get house price predictions."
    }

#  Define input data format
class HouseFeatures(BaseModel):
    OverallQual: float
    GrLivArea: float
    ExterQual: float
    KitchenQual: float
    GarageCars: float
    GarageArea: float
    TotalBsmtSF: float
    FirstFlrSF: float  
    BsmtQual: float

# Prediction endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = pd.DataFrame([features.dict()])

    # Rename FirstFlrSF to match model's feature name 1stFlrSF
    input_data.rename(columns={"FirstFlrSF": "1stFlrSF"}, inplace=True)

    # Debugging: Print column names
    print("Debugging: Final Input Columns →", input_data.columns.tolist())

    # Make prediction
    prediction = model.predict(input_data)[0]
    return {"predicted_price": round(prediction, 2)}







