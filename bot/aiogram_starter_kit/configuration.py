from dataclasses import dataclass

from decouple import config
from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    """
    Configuration for the database connection.

    Attributes:
        username (str): The database username.
        password (str): The database password.
        host (str): The database host.
        port (int): The database port.
        database (str): The name of the database.
        database_system (str): The database system (e.g., "postgresql").
        driver (str): The database driver (e.g., "asyncpg").

    Methods:
        build_connection_url(): Build a connection URL string based on the configuration.
    """

    username: str = config("POSTGRES_USER")
    password: str = config("POSTGRES_PASSWORD")
    host: str = config("POSTGRES_HOST")
    port: int = config("POSTGRES_PORT", cast=int)
    database: str = config("POSTGRES_DB")

    database_system: str = "postgresql"
    driver: str = "asyncpg"

    def build_connection_url(self) -> str:
        """
        Build a database connection URL based on the configuration.

        Returns:
            str: The database connection URL.
        """
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
    """
    Configuration for the Redis server connection.

    Attributes:
        host (str): The Redis server host.
        port (int): The Redis server port.
        db (int): The Redis database number.
    """

    host: str = config("REDIS_HOST")
    port: int = config("REDIS_PORT", cast=int)
    db: int = config("REDIS_DB", cast=int)


@dataclass
class BotConfig:
    """
    Configuration for the bot.

    Attributes:
        token (str): The bot API token.
    """

    token: str = config("BOT_TOKEN")


@dataclass
class Config:
    """
    Application configuration.

    Attributes:
        debug (bool): Whether the application is in debug mode.
        db (DatabaseConfig): Database configuration.
        redis (RedisConfig): Redis configuration.
        bot (BotConfig): Bot configuration.
    """

    debug: bool = config("DEBUG", cast=bool)

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()


# Create an instance of the Config class with the loaded configuration values
conf = Config()
