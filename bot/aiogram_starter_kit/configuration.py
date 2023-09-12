from dataclasses import dataclass

from decouple import config
from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    username: str = config("POSTGRES_USER")
    password: str = config("POSTGRES_PASSWORD")
    host: str = config("POSTGRES_HOST")
    port: int = config("POSTGRES_PORT", cast=int)
    database: str = config("POSTGRES_DB")

    database_system: str = "postgresql"
    driver: str = "asyncpg"

    def build_connection_url(self) -> str:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        ).render_as_string(hide_password=False)


@dataclass
class RedisConfig:
    host: str = config("REDIS_HOST")
    port: int = config("REDIS_PORT", cast=int)
    db: int = config("REDIS_DB", cast=int)


@dataclass
class BotConfig:
    token: str = config("BOT_TOKEN")


@dataclass
class Config:
    debug: bool = config("DEBUG", cast=bool)
    logging_level: int = config("LOGGING_LEVEL", cast=int)

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()


conf = Config()
