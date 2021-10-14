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
    return {  "fromDateTime": "2018-08-24T08:24:48.652Z",
    "tillDateTime": "2018-08-24T09:24:48.652Z",
    "values": [
      { "name": "PM1",          "value": 12.73   },
      { "name": "PM25",         "value": 18.7    },
      { "name": "PM10",         "value": 35.53   },
      { "name": "PRESSURE",     "value": 1012.62 },
      { "name": "HUMIDITY",     "value": 66.44   },
      { "name": "TEMPERATURE",  "value": 24.71   }
      ]}
    # if current_measurements is None:
    #     raise HTTPException(status_code=404, detail="Measurements not found")
    # return current_measurements


@router.get('/api/v1/measurements/history/', response_model=models.HistoricMeasurement)
async def get_history_measurement_by_coordinates(lat: float, long: float):
    measurements_repository = MeasurementRepository()
    historic_measurements = measurements_repository.get_historic_measurement_by_coordinates(
        lat, long)
    if historic_measurements is None:
        raise HTTPException(status_code=404, detail="Historic measurements not found")
    return historic_measurements


# @router.post("/users", response_model=schemas.User)
# @inject
# def create_user(
#     user: schemas.UserCreate,
#     user_service: UserService = Depends(Provide[Application.user.user_service]),
# ):

#     db_user = user_service.get_user_by_email(user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return user_service.create_user(user)


# @router.get("/users", response_model=List[schemas.User])
# @inject
# def read_users(
#     skip: int = 0,
#     limit: int = 100,
#     user_service: UserService = Depends(Provide[Application.user.user_service]),
# ):
#     users = user_service.get_users(skip=skip, limit=limit)
#     return users


# @router.get("/users/{user_id}", response_model=schemas.User)
# @inject
# def read_user(
#     user_id: int,
#     user_service: UserService = Depends(Provide[Application.user.user_service]),
# ):
#     db_user = user_service.get_user_by_id(user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.post("/users/{user_id}/items", response_model=schemas.Item)
# @inject
# def create_item_for_user(
#     user_id: int,
#     item: schemas.ItemCreate,
#     item_service: ItemService = Depends(Provide[Application.item.item_service]),
# ):
#     return item_service.create_item(item, user_id)


# @router.get("/items", response_model=List[schemas.Item])
# @inject
# def read_items(
#     skip: int = 0,
#     limit: int = 100,
#     item_service: ItemService = Depends(Provide[Application.item.item_service]),
# ):
#     items = item_service.get_items(skip=skip, limit=limit)
#     return items
