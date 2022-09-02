

from django.urls import path
from . import views
from product.views import GetProductsByCategory

urlpatterns = [
    path("<str:category_slug>/product/",GetProductsByCategory.as_view()),
    path("",views.IndustryListView.as_view()),
    path("<str:slug>/",views.IndustryDetailView.as_view())
]