from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_current_measurement_by_coordinates():
    response = client.get(
        "/api/v1/measurements/current/?lat=41.906551&long=12.453617")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {'from_date': '2021-10-18T09:06:35.404Z',
                               'till_date': '2021-10-18T10:06:35.404Z',
                               'values': [{'name': 'PM1', 'value': 16.66}, {'name': 'PM25', 'value': 24.54}, {
                                   'name': 'PM10', 'value': 39.67}, {'name': 'PRESSURE', 'value': 1025.07}, {'name': 'HUMIDITY', 'value': 91.12}, {'name': 'TEMPERATURE', 'value': 8.51}]}
