from enum import IntEnum

from pydantic_settings import BaseSettings


class DataSource(IntEnum):
    db = 0
    redis = 1


class Service(IntEnum):
    one = 0
    two = 1
    three = 2


class ClientASettings(BaseSettings):
    service: Service = Service.one
    data_source: DataSource = DataSource.db


class ClientBSettings(BaseSettings):
    service: Service = Service.two
    data_source: DataSource = DataSource.redis


class ClientCSettings(BaseSettings):
    service: Service = Service.three
    data_source: DataSource = DataSource.db
