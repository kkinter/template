from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "dummy"
    PGDATABASE_URL: Any = None
    ENVIRONMENT: str = "dev"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
