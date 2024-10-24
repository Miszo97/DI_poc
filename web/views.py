from dependency_injector.wiring import inject, Provide
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
@inject
def index(request, service=Provide["service"]):
    return Response({service.get()})
