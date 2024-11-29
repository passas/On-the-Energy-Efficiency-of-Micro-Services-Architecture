from rest_framework import serializers

from .models import Cart



class OrdersSerializer (serializers.Serializer):

    product_id = serializers.IntegerField()
    
    S = serializers.IntegerField()
    
    M = serializers.IntegerField()
    
    L = serializers.IntegerField()
    
    XL = serializers.IntegerField()

class CartSerializer (serializers.ModelSerializer):
    
    products = OrdersSerializer(many=True)

    class Meta:
    
        model = Cart
    
        fields = ["products"]

        