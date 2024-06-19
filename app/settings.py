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
    db_host: str = env.str("PGHOST")
    db_port: int = int(env.str("PGPORT"))
    db_user: str = env.str("PGUSER")
    db_password: str = env.str("PGPASSWORD")
    db_database: str = env.str("PGDATABASE")

    db_pool_size: int = 5
    db_max_overflow: int = 0
    db_echo: bool = False
    db_pool_pre_ping: bool = True

    app_port: int = int(env.str("PORT"))

    @property
    def db_dsn(self) -> URL:
        return URL.create(
            self.db_driver,
            self.db_user,
            self.db_password,
            self.db_host,
            self.db_port,
            self.db_database,
        )
        

settings = Settings()
