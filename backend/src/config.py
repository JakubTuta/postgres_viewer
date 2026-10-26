import functools

import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    is_docker: bool = pydantic.Field(default=False)

    postgres_host: str = pydantic.Field(default="localhost")
    postgres_port: int = pydantic.Field(default=5432)
    postgres_name: str = pydantic.Field(default="postgres_db")
    postgres_user: str = pydantic.Field(default="postgres")
    postgres_password: str = pydantic.Field(default="postgres")

    @pydantic.field_validator("is_docker")
    @classmethod
    def validate_is_docker(cls, value: str | int | bool) -> bool:
        return str(value).lower() in ["1", "true"]


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
