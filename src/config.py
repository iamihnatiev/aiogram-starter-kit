import logging

from dataclasses import dataclass

from decouple import config
from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    username: str = config('POSTGRES_USER')
    password: str | None = config('POSTGRES_PASSWORD', default=None)
    host: str = config('POSTGRES_HOST', default='postgres')
    port: int = config('POSTGRES_PORT', default=5432, cast=int)
    database: str = config('POSTGRES_DATABASE')

    database_system: str = 'postgresql'
    driver: str = 'asyncpg'

    def build_connection_url(self) -> str:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        ).render_as_string(hide_password=False)  # Required for Alembic


@dataclass
class RedisConfig:
    password: str = config('REDIS_PASSWORD')
    host: str = config('REDIS_HOST', default='redis')
    port: int = config('REDIS_PORT', default=6379, cast=int)
    db: int = config('REDIS_DATABASE', default=1, cast=int)

    state_ttl: int = config('REDIS_STATE_TTL', default=3600, cast=int)
    data_ttl: int = config('REDIS_DATA_TTL', default=86400, cast=int)


@dataclass
class BotConfig:
    token: str = config('BOT_TOKEN')


@dataclass
class Config:
    debug: bool = config('DEBUG', default=True, cast=bool)
    logging_level: int = config('LOGGING_LEVEL', default=logging.INFO, cast=int)

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()


conf = Config()
