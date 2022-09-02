from rest_framework import serializers
from .models import Product,ProductImage
from industry.serializer import IndustrySerializer

class ProudctImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['get_images',]

class ProductSerializer(serializers.ModelSerializer):
    images =  ProudctImageSerializer(many=True)
    industry = IndustrySerializer(read_only=True)
    class Meta:
        model =  Product
        fields = (
            "id",
            "slug",
            "productName",
            "brand",
            "price",
            "approved",
            "terms",
            "descripton",
            "industry",
            "images",
            # "get_absolute_url"
            )