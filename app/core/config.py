from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_version: str

    environment: str
    debug: bool

    weather_ingestion_limit: int = 60
    enable_scheduler: bool = True
    database_url: str

    weather_api_key: str
    weather_base_url: str
    weather_timeout: int = 10 

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()