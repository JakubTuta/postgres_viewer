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

    inside_container: bool = pydantic.Field(default=False)

    postgres_host: str = pydantic.Field(default="localhost")
    postgres_port: int = pydantic.Field(default=5432)
    postgres_service: str = pydantic.Field(default="postgres")
    postgres_name: str = pydantic.Field(default="postgres_db")
    postgres_user: str = pydantic.Field(default="postgres")
    postgres_password: str = pydantic.Field(default="postgres")

    @pydantic.field_validator("inside_container")
    @classmethod
    def validate_inside_container(cls, value: str | int | bool) -> bool:
        return str(value).lower() in ["1", "true"]

    @property
    def database_url(self) -> str:
        if self.inside_container:
            return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_service}/{self.postgres_name}"

        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_name}"


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
