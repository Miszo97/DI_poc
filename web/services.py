import abc

from web.data_sources import DataSource


class ServiceAbstract(abc.ABC):
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    @abc.abstractmethod
    def get(self):
        pass


class ServiceA(ServiceAbstract):

    def get(self):
        return f"Service A for data: {self.data_source.get_products()}"


class ServiceB(ServiceAbstract):
    def get(self):
        return f"Service B for data: {self.data_source.get_products()}"


class ServiceC(ServiceAbstract):
    def get(self):
        return f"Service C for data: {self.data_source.get_products()}"
