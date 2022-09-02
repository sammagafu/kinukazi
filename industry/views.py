from .serializer import IndustrySerializer
from rest_framework import generics
from .models import ProuctIndusty

class IndustryListView(generics.ListCreateAPIView):
    queryset = ProuctIndusty.objects.all()
    serializer_class = IndustrySerializer


class IndustryDetailView(generics.RetrieveAPIView):
    queryset = ProuctIndusty.objects.all()
    serializer_class = IndustrySerializer
    lookup_field = 'slug'