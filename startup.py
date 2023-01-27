from aiogram.types import BotCommand
from config import bot


async def set_bot_commands():
    await bot.set_my_commands(
        commands=[
            BotCommand(command="run", description="Начать Использование 🔥"),
            BotCommand(command="home", description="Управление Ботом ⛩"),
        ]
    )
