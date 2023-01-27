from dataclasses import dataclass
from os import environ
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

BOT_TOKEN = str(environ.get("BOT_TOKEN"))

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())


@dataclass(slots=True, frozen=True)
class BotPath:
    ROOT_DIR = Path(__file__).resolve().parent
    STATIC_DIR = ROOT_DIR / "static"
    LOGS_DIR = STATIC_DIR / "logs"


logger.add(BotPath.LOGS_DIR / "dev.log", format="{time} {level} {message}",
           level="DEBUG", rotation="1 MB", compression="zip")
