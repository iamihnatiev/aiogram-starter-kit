from os import getenv
from dataclasses import dataclass

from dotenv import load_dotenv

# Load environment variables from `.env` file
load_dotenv()


@dataclass
class BotConfig:
    token: str = getenv('BOT_TOKEN')


@dataclass
class Config:
    bot = BotConfig()


conf = Config()
