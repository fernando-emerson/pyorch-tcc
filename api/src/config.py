from functools import lru_cache
from pydantic_settings import BaseSettings
import decouple
from pydantic_settings import SettingsConfigDict


# looks at them as a case-insensitive (validate them)
# default values provided
class Settings(BaseSettings):
    # General settings
    TITLE: str = "FastAPI App"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str | None = None
    DEBUG: bool = False
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    SERVER_HOST: str = decouple.config("SERVER_HOST", cast=str)
    SERVER_PORT: int = decouple.config("SERVER_PORT", cast=int)
    SERVER_WORKERS: int = decouple.config("SERVER_WORKERS", cast=int)

    # Database settings
    DB_HOST: str = decouple.config("DB_HOST", cast=str)
    DB_MAX_POOL_CON: int = decouple.config("DB_MAX_POOL_CON", cast=int)
    DB_NAME: str = decouple.config("DB_NAME", cast=str)
    DB_PASSWORD: str = decouple.config("DB_PASSWORD", cast=str)
    DB_POOL_SIZE: int = decouple.config("DB_POOL_SIZE", cast=int)
    DB_POOL_OVERFLOW: int = decouple.config("DB_POOL_OVERFLOW", cast=int)
    DB_PORT: int = decouple.config("DB_PORT", cast=int)
    DB_SCHEMA: str = decouple.config("DB_SCHEMA", cast=str)
    DB_TIMEOUT: int = decouple.config("DB_TIMEOUT", cast=int)
    DB_USERNAME: str = decouple.config("DB_USERNAME", cast=str)

    # Celery settings
    BROKER_URL: str = decouple.config("BROKER_URL", cast=str)
    RESULT_BACKEND: str = decouple.config("RESULT_BACKEND", cast=str)

    model_config = SettingsConfigDict(
        validate_assignment=True, case_sensitive=True, env_file=".env"
    )

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "redoc_url": self.REDOC_URL,
            "api_prefix": self.API_PREFIX,
        }


@lru_cache()
def get_settings() -> Settings:
    return Settings()


get_settings.cache_clear()

settings: Settings = get_settings()
