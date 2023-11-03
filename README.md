# VehicleCO2Emissions
 
run ```uvicorn API:app --reload```

## Testing

Open postman and send a post request with the required parameters: 

```{
    "EngineSize_L": 2.0,
    "Cylinders": 12,
    "Transmission": "M6",
    "Fuel_Type": "D",
    "FuelConsumptionComb_L_per_100_km": 500
}```