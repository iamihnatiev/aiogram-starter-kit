from os import getenv
from dataclasses import dataclass

from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    username: str = getenv(key='POSTGRES_USER', default='postgres')
    password: str | None = getenv(key='POSTGRES_PASSWORD', default='postgres')
    host: str = getenv(key='POSTGRES_HOST', default='postgres')
    port: int = int(getenv(key='POSTGRES_PORT', default=5432))
    database: str = getenv(key='POSTGRES_NAME')

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
class BotConfig:
    token: str = getenv('BOT_TOKEN')


@dataclass
class Config:
    db = DatabaseConfig()
    bot = BotConfig()


conf = Config()
