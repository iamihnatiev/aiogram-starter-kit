import logging

from os import getenv
from dataclasses import dataclass

from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    username: str = getenv(key='POSTGRES_USER')
    password: str | None = getenv(key='POSTGRES_PASSWORD', default=None)
    host: str = getenv(key='POSTGRES_HOST', default='postgres')
    port: int = int(getenv(key='POSTGRES_PORT', default=5432))
    database: str = getenv(key='POSTGRES_DATABASE')

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
        ).render_as_string()


@dataclass
class RedisConfig:
    username: str = getenv(key='REDIS_USER')
    password: str = getenv(key='REDIS_PASSWORD')
    host: str = getenv(key='REDIS_HOST', default='redis')
    port: int = int(getenv(key='REDIS_PORT', default=6379))
    db: int = int(getenv(key='REDIS_DB', default=1))

    state_ttl: int | None = getenv(key='REDIS_STATE_TTL', default=None)
    data_ttl: int | None = getenv(key='REDIS_DATA_TTL', default=None)


@dataclass
class BotConfig:
    token: str = getenv('BOT_TOKEN')


@dataclass
class Config:
    logging_level = int(getenv('LOGGING_LEVEL', logging.INFO))

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()


conf = Config()
