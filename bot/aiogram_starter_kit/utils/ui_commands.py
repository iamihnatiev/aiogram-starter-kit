from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_ui_commands(bot: Bot) -> None:
    """
    Set the user interface (UI) commands for the bot.

    This function sets custom commands for the bot, which users can invoke in chat to interact with it.

    Args:
        bot (Bot): The Aiogram Bot instance.
    """
    commands = [
        BotCommand(command="start", description="Start the bot"),
    ]

    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats(),
    )
