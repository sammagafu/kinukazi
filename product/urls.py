from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("",views.ProductListview.as_view(),name="list"),
    path("<slug:category_slug>/<slug:product_slug>/",views.ProductDetailView.as_view(),name="details"),
]