from rest_framework import serializers
from .models import Category
from .models import Product



class CategorySerializer (serializers.ModelSerializer):

    class Meta:
        
        model = Category

        fields = ["category"]



class PriceSerializer(serializers.Serializer):

    price = serializers.DecimalField(max_digits=7, decimal_places=2)

    discount = serializers.IntegerField()

class MaterialsSerializer (serializers.Serializer):

    material = serializers.CharField(max_length=16)

    percentage = serializers.IntegerField()

class StockSerializer (serializers.Serializer):

    S = serializers.IntegerField()

    M = serializers.IntegerField()
    
    L = serializers.IntegerField()
    
    XL = serializers.IntegerField()

class ProductSerializer (serializers.ModelSerializer):

    sex = serializers.StringRelatedField()

    category = serializers.StringRelatedField()
    
    color = serializers.StringRelatedField()
    
    price = PriceSerializer()
    
    materials = MaterialsSerializer(many=True)

    stock = StockSerializer()

    price_today = serializers.DecimalField(max_digits=7, decimal_places=2)

    class Meta:

        model = Product

        fields = ["id", "sku", "name", "materials", "sex", "color", "category", "price", "description", "stock", "price_today"]

        