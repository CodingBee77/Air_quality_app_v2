from app.models import CurrentMeasurement
from app.utils.obj_mapper import ObjectMapper
import requests
from app.config import settings


class MeasurementRepository:
    def __init__(self):
        pass

    def get_current_measurement_by_coordinates(self, lat: float, long: float) -> CurrentMeasurement:
        api_request = requests.get(
            "https://airapi.airly.eu/v2/measurements/nearest?lat=" +
            str(lat) + "&lng=" + str(long) + "&maxDistanceKM=2&maxResults=1",
            headers={'apikey': settings.AIRLY_API_KEY})
        current_measurement = ObjectMapper.map_current_measurement(api_request)
        return current_measurement

    # def get_user_by_email(self, email: str):
    #     with self.session_factory() as session:
    #         return session.query(User).filter(User.email == email).first()

    # def get_users(self, skip: int = 0, limit: int = 100):
    #     with self.session_factory() as session:
    #         return session.query(User).offset(skip).limit(limit).all()

    # def create_user(self, user: UserCreate):
    #     with self.session_factory() as session:
    #         db_user = User(email=user.email)
    #         session.add(db_user)
    #         session.commit()
    #         session.refresh(db_user)
    #         return db_user
