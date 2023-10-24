from rest_framework import serializers
from api.models import Product
    

class ProductSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='status_enum', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ['status', 'quantity']
