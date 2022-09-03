from pydantic import BaseSettings, PostgresDsn, validator, AnyHttpUrl
from typing import Any


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    URL: str
    # We need this first to get the total of free games to loop through.
    FIRST_GAME_ARIA: str
    XPATH_GAME: str
    XPATH_TIME: str
    SELENIUM_GRID_HOST: str

    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True



settings = Settings()