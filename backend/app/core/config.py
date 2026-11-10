
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "QuizAI"
    environment: str = "local"
    debug: bool = True

    secret_key: str = "temporary-dev-secret-key-change-me"
    database_url: str = (
        "postgresql+psycopg://quizai_user:quizai_secure_password@localhost:5432/quizai_db"
    )

    cors_origins: list[str] = ["http://localhost:3000"]


settings = Settings()
