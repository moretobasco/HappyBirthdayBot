from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    не забыть добавить переменные окружения .env в конфигурации IDE
    """

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SMTP_USER: str
    SMTP_PASS: str
    SMTP_HOST: str
    SMTP_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    RABBITMQ_DEFAULT_HOST: str
    RABBITMQ_DEFAULT_PORT: int
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str

    ADMIN_TELEGRAM: int

    LOCALHOST: str

    @property
    def DATABASE_URL(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def RABBITMQ_URL(self) -> str:
        return f"amqp://{self.RABBITMQ_DEFAULT_USER}:{self.RABBITMQ_DEFAULT_PASS}@{self.RABBITMQ_DEFAULT_HOST}:{self.RABBITMQ_DEFAULT_PORT}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()