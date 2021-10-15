from app.models import CurrentMeasurement, ChartMeasurement
import json


class ObjectMapper:
    def map_current_measurement(self, response: json) -> CurrentMeasurement:
        current_measurement = None
        try:
            api = json.loads(response.content)
            current_measurement = CurrentMeasurement(from_date=str(api["current"]["fromDateTime"]), till_date=str(
                api["current"]["tillDateTime"]), values=api["current"]["values"])
        except Exception as e:
            print(e)

        return current_measurement

    def map_chart_measurement(self, response: json) -> ChartMeasurement:
        historic_measurement = None
        try:
            api = json.loads(response.content)
            labels, data = self._convert_data_for_chart(api)
            historic_measurement = ChartMeasurement(
                labels=labels, datasets=data)

        except Exception as e:
            print(e)

        return historic_measurement

    def _get_index_value(self, index_name, values_list):
        """Return value for PM1 or PM10 or PM25"""
        index_value = [element["value"]
                       for element in values_list if element["name"] == index_name]
        return index_value[0]

    def _append_index_values_to_dict(self, index_object, index_name, history_dict):
        return index_object["data"].append(self._get_index_value(index_name=index_name, values_list=history_dict["values"]))

    def _convert_data_for_chart(self, api_response):
        labels = []
        datasets = []

        #TODO: refactor code to remove hardcoded indexes
        index_PM1 = {'label': "PM1", 'data': []}
        index_PM10 = {'label': "PM10", 'data': []}
        index_PM25 = {'label': "PM25", 'data': []}

        for elem in api_response.get("history"):
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
