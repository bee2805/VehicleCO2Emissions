# VehicleCO2Emissions
 
run ```uvicorn API:app --reload```

## Testing

Open your chosen API platform and send a post request with the required parameters: 

```
{
    "EngineSize_L": float,
    "Cylinders": int,
    "Transmission": str,
    "Fuel_Type": str,
    "FuelConsumptionComb_L_per_100_km": float
}
```