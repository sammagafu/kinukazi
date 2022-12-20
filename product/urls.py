from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("",views.MachineListview.as_view(),name="list"),
    path("<slug:category_slug>/<slug:product_slug>/",views.MachineDetailView.as_view(),name="details"),
]