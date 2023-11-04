# VehicleCO2Emissions

This API allows you to predict the emissions of your vehicle based on certain parameters, such as engine size, amount of cylinders and gears, your transmission type and fuel consumption.

## Running the API
 
run ```uvicorn API:app --reload``` in your terminal

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