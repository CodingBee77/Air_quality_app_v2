from app.models import CurrentMeasurement, HistoricMeasurement
from app.mappers.obj_mapper import ObjectMapper
import requests
from app.config import settings


class MeasurementRepository:
    def __init__(self):
        pass

#TODO: create API client
    #  def get_current_measurement_by_coordinates(self, lat: float, long: float) -> CurrentMeasurement:
    #      mesurement_response = client.get_measurement(lat, lang)
    #      current_meas = ObjectMapper.map_current_measurement(mesurement_response)
    #      return current_meas

    def get_current_measurement_by_coordinates(self, lat: float, long: float) -> CurrentMeasurement:
        api_request = requests.get(
            "https://airapi.airly.eu/v2/measurements/nearest?lat=" +
            str(lat) + "&lng=" + str(long) + "&maxDistanceKM=2&maxResults=1",
            headers={'apikey': settings.AIRLY_API_KEY})
        # print(api_request)
        mapper = ObjectMapper()
        current_measurement = mapper.map_current_measurement(api_request)
        return current_measurement


    def get_chart_measurement_by_coordinates(self, lat: float, long: float) -> HistoricMeasurement:
        api_request = requests.get(
            "https://airapi.airly.eu/v2/measurements/nearest?lat=" +
            str(lat) + "&lng=" + str(long) + "&maxDistanceKM=2&maxResults=1",
            headers={'apikey': settings.AIRLY_API_KEY})
        # print(api_request)
        mapper = ObjectMapper()
        historic_measurement = mapper.map_chart_measurement(response=api_request)
        return historic_measurement
