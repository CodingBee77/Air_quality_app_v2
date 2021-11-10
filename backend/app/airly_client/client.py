import requests
from app.config import settings
import json

class AirlyClient:
    def get_measurement(lat: float, long: float)-> json:
        api_response = None
        try:
            api_response = requests.get(
            "https://airapi.airly.eu/v2/measurements/nearest?lat=" +
            str(lat) + "&lng=" + str(long) + "&maxDistanceKM=2&maxResults=1",
            headers={'apikey': settings.AIRLY_API_KEY})
        except requests.exceptions.RequestException as e:
            print(e)
            
        return api_response

            
