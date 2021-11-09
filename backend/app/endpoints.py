from typing import List
from fastapi import APIRouter, HTTPException
from . import models
from .repositories.measurements_repository import MeasurementRepository

router = APIRouter()


@router.get('/api/v1/measurements/current/')
# response_model=models.CurrentMeasurement
async def get_current_measurement_by_coordinates(lat: float, long: float):
    # measurements_repository = MeasurementRepository()
    # current_measurements = measurements_repository.get_current_measurement_by_coordinates(
    #     lat, long)
    return {"fromDateTime": "2018-08-24T08:24:48.652Z",
            "tillDateTime": "2018-08-24T09:24:48.652Z",
            "values": [
                {"name": "PM1",          "value": 12.73},
                {"name": "PM25",         "value": 18.7},
                {"name": "PM10",         "value": 35.53},
                {"name": "PRESSURE",     "value": 1012.62},
                {"name": "HUMIDITY",     "value": 66.44},
                {"name": "TEMPERATURE",  "value": 24.71}
            ]}
    # if current_measurements is None:
    #     raise HTTPException(status_code=404, detail="Measurements not found")
    # return current_measurements


@router.get('/api/v1/measurements/history/', response_model=models.ChartMeasurement)
async def get_history_measurement_by_coordinates(lat: float, long: float):
    measurements_repository = MeasurementRepository()
    historic_measurements = measurements_repository.get_chart_measurement_by_coordinates(
        lat, long, data_type="history")
    if historic_measurements is None:
        raise HTTPException(
            status_code=404, detail="Historic measurements not found")
    return historic_measurements


@router.get('/api/v1/measurements/forecast/', response_model=models.ChartMeasurement)
async def get_forecast_measurement_by_coordinates(lat: float, long: float):
    measurements_repository = MeasurementRepository()
    forecast_measurements = measurements_repository.get_chart_measurement_by_coordinates(
        lat, long, data_type="forecast")
    if forecast_measurements is None:
        raise HTTPException(
            status_code=404, detail="Forecast measurements not found")
    return forecast_measurements


@router.get('/api/v1/measurements/standards/', response_model=models.StandardFactors)
async def get_standards_by_coordinates(lat: float, long: float):
    measurements_repository = MeasurementRepository()
    standard_factors = measurements_repository.get_standards_by_coordinates(
        lat, long)
    if standard_factors is None:
        raise HTTPException(
            status_code=404, detail="Standards not found")
    return standard_factors


