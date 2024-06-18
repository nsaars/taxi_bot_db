import pydantic_settings
from granian.log import LogLevels
from sqlalchemy.engine.url import URL
from environs import Env

env = Env()
env.read_env()

class Settings(pydantic_settings.BaseSettings):
    service_name: str = "taxi_database"
    debug: bool = True
    log_level: LogLevels = LogLevels.info

    db_driver: str = "postgresql+asyncpg"
    db_url: str = env.str("DATABASE_URL")

    db_pool_size: int = 5
    db_max_overflow: int = 0
    db_echo: bool = False
    db_pool_pre_ping: bool = True

    app_port: int = 8000

    @property
    def db_dsn(self) -> URL:
        return db_url


settings = Settings()
