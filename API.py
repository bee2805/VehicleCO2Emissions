from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from pydantic import BaseModel
import os
import joblib

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers
)

# Loading model
vehicle_emissions_model = joblib.load("vehicle_emissions_model.pkl")

# Desfining a model to specify the expected input format
class InputData(BaseModel):
    engine_size: int
    cyliners: int
    transmission: str
    fuel_type: str
    fuel_consumption: int

@app.post("/predict_vehicle_emissions")
def predict_vehicle_emissions():
    return {"message": "ENDPOINT FUNCTIONALITY PENDING"}

# implementing default API endpoint
@app.get("/") # defining url extension of endpoint
def read_root():
    return {"message": "Fast API setup successfully"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run(app, host="0.0.0.0", port=port)