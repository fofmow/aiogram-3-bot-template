import asyncio
import logging

from config import bot
from handlers import dp
from startup import set_bot_commands

logging.basicConfig(level=logging.INFO)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_commands()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
