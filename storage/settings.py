from pathlib import Path

from peewee import SqliteDatabase
from pytz import timezone

DB_DIR = Path(__file__).resolve().parent
base = SqliteDatabase(DB_DIR / "db.sqlite3")

MOSCOW_TZ = timezone("Europe/Moscow")

DT_FORMAT = "%Y-%m-%d %H:%M:%S"
