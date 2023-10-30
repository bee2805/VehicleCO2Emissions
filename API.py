from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class input_model(BaseModel):
    EngineSizeL: float
    Cylinders: int
    Transmission: str
    FuelType: str
    FuelConsumptionComb: float

vehicle_emissions_model = joblib.load("vehicle_emissions_model.pkl")

@app.post('/')
async def endpoint(data: input_model):
    return data