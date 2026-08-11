from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "CineMatch API"
    API_V1_STR: str = "/api/v1"

    # URL de connexion
    DATABASE_URL: str = "postgresql://cinematch_user:cinematch_password@localhost:5433/cinematch_db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # API Clé TMDb
    TMDB_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()