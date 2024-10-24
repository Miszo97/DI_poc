from abc import ABC


class DataSource(ABC):
    def get_products(self):
        pass


class DataBaseDataSource(DataSource):
    def get_products(self):
        return "Data from database"


class RedisDataSource(DataSource):
    def get_products(self):
        return "Data from redis"