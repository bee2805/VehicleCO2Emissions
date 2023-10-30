from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class InputModel(BaseModel):
    EngineSizeL: float
    Cylinders: int
    Transmission: str
    FuelType: str
    FuelConsumptionComb: float

# Loading model
vehicle_emissions_model = joblib.load("vehicle_emissions_model.pkl")

@app.post('/')
async def endpoint(data: InputModel):
    try:
        # Create a DataFrame from the input data
        df = pd.DataFrame([data.model_dump()])

        # Make predictions using the loaded model
        prediction = vehicle_emissions_model.predict(df)

        # Return the prediction
        return {"prediction": int(prediction)}
    except Exception as e:
        # Handling errors
        raise HTTPException(status_code=500, detail=str(e))
