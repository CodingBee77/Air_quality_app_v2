from pydantic import BaseSettings


class Settings(BaseSettings):
    AIRLY_API_KEY: str = ''


settings = Settings()