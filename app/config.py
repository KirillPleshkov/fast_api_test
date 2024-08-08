import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class BaseServiceSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"),
        extra="ignore",
    )


class Postgres(BaseServiceSettings):
    DB_HOST: str = Field(alias="POSTGRES_HOST")
    DB_PORT: int = Field(alias="POSTGRES_PORT")
    DB_NAME: str = Field(alias="POSTGRES_DB")
    DB_USER: str = Field(alias="POSTGRES_USER")
    DB_PASSWORD: str = Field(alias="POSTGRES_PASSWORD")


class Settings(BaseServiceSettings):
    database: Postgres = Postgres()


settings = Settings()


def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.database.DB_USER}:{settings.database.DB_PASSWORD}@"
        f"{settings.database.DB_HOST}:{settings.database.DB_PORT}/{settings.database.DB_NAME}"
    )
