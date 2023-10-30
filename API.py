from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class input_model(BaseModel):
    EngineSizeL: float
    Cylinders: int
    Transmission: str
    FuelType: str
    FuelConsumptionComb: float


@app.get('/')
async def endpoint():
    return {"message": "Endpoint set up successfully"}