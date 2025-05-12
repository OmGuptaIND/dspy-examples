from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # --- Project ---
    project_name: str = Field(default="Shooting Star", alias="PROJECT_NAME")

    # --- Run Time ---
    environment: str = Field(default="development", alias="ENVIRONMENT")
    log_level: str = Field(default="info", alias="LOG_LEVEL")

    # --- API Credentials ---
    gemini_api_key: str = Field(alias="GEMINI_API_KEY")
    fal_api_key: str = Field(alias="FAL_API_KEY")


    model_config = SettingsConfigDict(
        env_file='.env',        
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'         
    )

settings = Settings() # type: ignore[call-arg]