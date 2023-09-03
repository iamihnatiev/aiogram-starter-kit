from os import getenv
from dataclasses import dataclass

from sqlalchemy.engine import URL

from dotenv import load_dotenv

# Load environment variables from `.env` file
load_dotenv()


@dataclass
class DatabaseConfig:
    username: str = getenv('POSTGRES_USER', 'root')
    password: str | None = getenv('POSTGRES_PASSWORD', None)
    host: str = getenv('POSTGRES_HOST', 'localhost')
    port: int = int(getenv('POSTGRES_PORT', 5432))
    database: str = getenv('POSTGRES_NAME', 'db')

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
