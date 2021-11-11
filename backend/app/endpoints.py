from typing import List
from fastapi import APIRouter, HTTPException
from . import models
from .repositories.measurements_repository import MeasurementRepository

router = APIRouter()


@router.get('/api/v1/measurements/current/', response_model=models.CurrentMeasurement)
async def get_current_measurement_by_coordinates(lat: float, long: float):
    measurements_repository = MeasurementRepository()
    current_measurements = measurements_repository.get_current_measurement_by_coordinates(
        lat, long)
    # return {'from_date': '2021-10-18T09:06:35.404Z', 
    # 'till_date': '2021-10-18T10:06:35.404Z', 
    # 'values': [{'name': 'PM1', 'value': 16.66}, 
    # {'name': 'PM25', 'value': 24.54}, 
    # {'name': 'PM10', 'value': 39.67}, 
    # {'name': 'PRESSURE', 'value': 1025.07}, 
    # {'name': 'HUMIDITY', 'value': 91.12}, 
    # {'name': 'TEMPERATURE', 'value': 8.51}]}
    if current_measurements is None:
        raise HTTPException(status_code=404, detail="Measurements not found")
    return current_measurements


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
