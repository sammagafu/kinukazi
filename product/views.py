from django.http import Http404
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product
from rest_framework import generics,filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from industry.models import ProuctIndusty,ProductSemiIndusry


# Create your views here.
class MachineListview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields = ['industry', 'price','terms']
    ordering_fields = ['price','created_at']
    search_fields = ['productName', 'descripton']

class MachineDetailView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class GetMachinesByCategory(APIView):
    def get_object(self, category_slug):
        try:
            return ProuctIndusty.objects.filter(category__slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        product = self.get_object(category_slug)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)