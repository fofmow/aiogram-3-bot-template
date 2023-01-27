from peewee import Model
from .settings import base


class BaseModel(Model):
    class Meta:
        database = base
