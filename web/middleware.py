# web/middleware.py
from django.utils.deprecation import MiddlewareMixin
from dependency_injector import providers
import web.data_sources
import web.services
import web.serializers
from web import dynamic_services
from DI_poc.settings import services_config


class ClientMiddleware(MiddlewareMixin):
    def process_request(self, request):
        client = request.headers.get('CLIENT')
        if client and client in services_config:
            data_source_class = getattr(web.data_sources, services_config[client]["data_source"]["class"])
            service_class = getattr(web.services, services_config[client]["service"]["class"])
            serializer_class = getattr(web.serializers, services_config[client]["serializer"]["class"])
            dynamic_services.data_source = providers.Factory(data_source_class)
            dynamic_services.serializer_class = providers.Object(serializer_class)
            dynamic_services.service = providers.Factory(service_class, data_source=dynamic_services.data_source)
            dynamic_services.wire(modules=[".views"])

