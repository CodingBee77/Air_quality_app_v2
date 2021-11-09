from app.models import CurrentMeasurement, IndexMeasurement, ChartMeasurement, StandardFactorMeasurement, StandardFactors
import json
from typing import Tuple


IGNORED_INDEXES = ("PRESSURE", "HUMIDITY", "TEMPERATURE")

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

    def map_chart_measurement(self, response: json, data_type: str) -> ChartMeasurement:
        chart_measurement = None
        # api = self._load_response(response)
        api = response
        try:
            labels, data = self._convert_data_for_chart(
                api, data_type=data_type)
            chart_measurement = ChartMeasurement(
                labels=labels, datasets=data)

        except Exception as e:
            print(e)

        return chart_measurement

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

    def _create_index_dict(self, values_object):
        index_dicts = {}
        for elem in values_object:
            index_name = elem.get("name")
            if index_name in IGNORED_INDEXES:
                continue 
            index_dict = { "label": index_name, "data": []}
            index_dicts[index_name] = index_dict

        return index_dicts

    # def _get_index_value(self, index_name: str, values_list: list) -> float:
    #     """Return value for PM1 or PM10 or PM25"""
    #     index_value = [element["value"]
    #                    for element in values_list if element["name"] == index_name]
    #     return index_value[0]

    # def _append_index_values_to_dict(self, index_object: dict, index_name: str, history_dict: dict) -> dict:
    #     return index_object["data"].append(self._get_index_value(index_name=index_name, values_list=history_dict["values"]))

    def _convert_data_for_chart(self, api_response: dict, data_type: str) -> Tuple[list, list]:
        labels = []
        datasets = []
        color_list = ["#51B8A9A8", "#e28743A8", "#25b836A8", "#1aadbaA8","#1a1abaA8"]
        indexes_map = self._create_index_dict(api_response.get(data_type)[0]["values"])
        

        for elem in api_response.get(data_type):
            dt_obj_converted = elem["fromDateTime"][:16].replace("T", " ")
            labels.append(dt_obj_converted)
            for hist_value in elem["values"]:
                if hist_value["name"] in IGNORED_INDEXES:
                    continue
                indexes_map[hist_value["name"]]["data"].append(hist_value["value"])

        set_color = 0
        for key, value in indexes_map.items():
            datasets.append(IndexMeasurement(label=key, backgroundColor=color_list[set_color], data= value["data"]))
            set_color += 1


        return labels, datasets