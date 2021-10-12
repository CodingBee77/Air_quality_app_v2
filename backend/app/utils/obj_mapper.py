from app.models import CurrentMeasurement
import json


class ObjectMapper:

    @staticmethod
    def map_current_measurement(response: json) -> CurrentMeasurement:
        current_measurement = None
        try:
            api = json.loads(response.content)
            current_measurement = CurrentMeasurement(from_date=str(api["current"]["fromDateTime"]), till_date=str(
                api["current"]["tillDateTime"]), values=api["current"]["values"])
        except Exception as e:
            print(e)

        return current_measurement
