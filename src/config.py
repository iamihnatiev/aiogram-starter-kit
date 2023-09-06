import logging

from os import getenv
from dataclasses import dataclass

from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    username: str = getenv(key='POSTGRES_USER', default='postgres')
    password: str | None = getenv(key='POSTGRES_PASSWORD', default='postgres')
    host: str = getenv(key='POSTGRES_HOST', default='postgres')
    port: int = int(getenv(key='POSTGRES_PORT', default=5432))
    database: str = getenv(key='POSTGRES_DATABASE')

    database_system: str = 'postgresql'
    driver: str = 'asyncpg'

    def build_connection_url(self) -> URL:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )


@dataclass
class RedisConfig:
    username: str = getenv(key='REDIS_USER', default='redis')
    password: str | None = getenv(key='REDIS_PASSWORD', default='redis')
    host: str = getenv(key='REDIS_HOST', default='redis')
    port: int = int(getenv(key='REDIS_PORT', default=6379))
    db: int = int(getenv(key='REDIS_DB', default=1))

    state_ttl: int = int(getenv(key='REDIS_STATE_TTL', default=0))
    data_ttl: int = int(getenv(key='REDIS_DATA_TTL', default=0))


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
