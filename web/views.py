from dependency_injector.wiring import inject, Provide
from rest_framework import viewsets, permissions, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web.models import Product
from web.serializers import ProductSerializer


@api_view(('GET',))
@inject
def index(request, service=Provide["service"]):
    return Response({service.get()})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    @inject
    def perform_create(self, serializer, service=Provide["service"]):
        serializer.validated_data["product_id"] = service.get()
        serializer.save()

    @inject
    def get_serializer_class(self, serializer_class=Provide["serializer_class"], *args, **kwargs):
        if not issubclass(serializer_class, serializers.ModelSerializer):
            return ProductSerializer
        return serializer_class
