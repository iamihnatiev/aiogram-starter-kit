import asyncio
import logging
import sys

from aiogram_starter_kit import start_bot


if __name__ == "__main__":
    # Configure logging to display log messages on the console
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # Run the Telegram bot using asyncio
    asyncio.run(start_bot())
