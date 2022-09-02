from rest_framework import serializers
from .models import ProuctIndusty,ProductSemiIndusry


class SubIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSemiIndusry
        fields = ['subcategoryname', 'slug']

class IndustrySerializer(serializers.ModelSerializer):
    subcategory = SubIndustrySerializer(many=True, read_only=True)

    class Meta:
        model = ProuctIndusty
        fields = ['id','categoryname', 'slug','subcategory']