from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): # load enviourment variables
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    RAPID_API_KEY: str
    GROQ_API_KEY: str

    model_config = SettingsConfigDict(env_file="D:/SmartCRUD/.env", extra="ignore")

settings = Settings()