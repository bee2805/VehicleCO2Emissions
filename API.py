from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

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

class InputModel(BaseModel):
    EngineSize_L: float
    Cylinders: int
    Transmission: str
    Fuel_Type: str
    FuelConsumptionComb_L_per_100_km: float

# Loading model and transformer
vehicle_emissions_model = joblib.load("vehicle_emissions_model.pkl")
transformed_data = joblib.load("transformed_data.pkl")

@app.post('/')
async def endpoint(data: InputModel):
    try:
        # Creating a DataFrame from the input data
        df = pd.DataFrame([data.dict()])

        # Rename columns to match original data
        df = df.rename(columns={
            'EngineSize_L': 'Engine Size(L)',
            'Fuel_Type': 'Fuel Type',
            'FuelConsumptionComb_L_per_100_km': 'Fuel Consumption Comb (L/100 km)'
        })

        # Apply the same transformation to the input data
        df = transformed_data.transform(df)

        # Make predictions using the loaded model
        prediction = vehicle_emissions_model.predict(df)

        # Return the prediction
        return {"prediction": int(prediction)}
    except Exception as e:
        # Handling errors
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run(app, host="0.0.0.0", port=port)
