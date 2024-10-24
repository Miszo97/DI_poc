from rest_framework import serializers

from web.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientAProductSerializer(ProductSerializer):
    def validate_extra_info(self, value):
        if not value.get('size'):
            raise serializers.ValidationError("Product should have size")
        return value


class ClientBProductSerializer(ProductSerializer):
    def validate_extra_info(self, value):
        if not value.get('color'):
            raise serializers.ValidationError("Product should have color")
        return value


class ClientCProductSerializer(ProductSerializer):
    def validate_extra_info(self, value):
        if not value.get('volume'):
            raise serializers.ValidationError("Product should have volume")
        return value
