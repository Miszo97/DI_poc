from django.apps import AppConfig
from . import dynamic_services


class WebConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "web"

    def ready(self):
        dynamic_services.wire(modules=[".views"])
