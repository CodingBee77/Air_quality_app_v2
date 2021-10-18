from app.models import CurrentMeasurement, ChartMeasurement, HistoricMeasurement, StandardFactorMeasurement, StandardFactors
import json
from typing import Tuple


class ObjectMapper:
    def map_current_measurement(self, response: json) -> CurrentMeasurement:
        current_measurement = None
        # api = self._load_response(response)
        api = response
        try:
            current_measurement = CurrentMeasurement(from_date=str(api["current"]["fromDateTime"]), till_date=str(
                api["current"]["tillDateTime"]), values=api["current"]["values"])
        except Exception as e:
            print(e)

        return current_measurement

    def map_chart_measurement(self, response: json, data_type: str) -> HistoricMeasurement:
        historic_measurement = None
        # api = self._load_response(response)
        api = response
        try:
            labels, data = self._convert_data_for_chart(
                api, data_type=data_type)
            historic_measurement = HistoricMeasurement(
                labels=labels, datasets=data)

        except Exception as e:
            print(e)

        return historic_measurement

    def map_standard_factor(self, response: json) -> StandardFactors:
        # response = self._load_response(response)

        if not response["current"]["standards"]:
            return None

        standard_factors_temp = []

        for elem in response["current"]["standards"]:
            standard = StandardFactorMeasurement(
                organization_name=elem["name"], pollutant=elem["pollutant"], limit=elem["limit"], percent=elem["percent"])
            standard_factors_temp.append(standard)

        standard_factors = StandardFactors(factors=standard_factors_temp)
        return standard_factors

    def _load_response(self, response: json) -> dict:
        response_dict = None
        try:
            response_dict = json.loads(response.content)

        except Exception as e:
            print(e)

        return response_dict

    def _get_index_value(self, index_name: str, values_list: list) -> float:
        """Return value for PM1 or PM10 or PM25"""
        index_value = [element["value"]
                       for element in values_list if element["name"] == index_name]
        return index_value[0]

    def _append_index_values_to_dict(self, index_object: dict, index_name: str, history_dict: dict) -> dict:
        return index_object["data"].append(self._get_index_value(index_name=index_name, values_list=history_dict["values"]))

    def _convert_data_for_chart(self, api_response: dict, data_type: str) -> Tuple[list, list]:
        labels = []
        datasets = []

        # TODO: refactor code to remove hardcoded indexes: it also remove issue with drawing forecast data chart
        index_PM1 = {'label': "PM1", 'data': []}
        index_PM10 = {'label': "PM10", 'data': []}
        index_PM25 = {'label': "PM25", 'data': []}

        for elem in api_response.get(data_type):
            dt_obj_converted = elem["fromDateTime"][:16].replace("T", " ")
            labels.append(dt_obj_converted)
            for (index_object, index_name, history_dict) in [(index_PM1, "PM1", elem), (index_PM10, "PM10", elem), (index_PM25, "PM25", elem)]:
                self._append_index_values_to_dict(
                    index_object, index_name, history_dict)

        chart_measurement_index_PM1 = ChartMeasurement(
            label=index_PM1["label"], backgroundColor="#AF09EB74", data=index_PM1["data"])
        chart_measurement_index_PM10 = ChartMeasurement(
            label=index_PM10["label"], backgroundColor="#09EB4C74", data=index_PM10["data"])
        chart_measurement_index_PM25 = ChartMeasurement(
            label=index_PM25["label"], backgroundColor="#EB9A0985", data=index_PM25["data"])

        for measurement_index in (chart_measurement_index_PM1, chart_measurement_index_PM10, chart_measurement_index_PM25):
            datasets.append(measurement_index)

        return labels, datasets
