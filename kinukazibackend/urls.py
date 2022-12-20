from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/machine/', include('product.urls')),
    path('api/v1/industry/', include('industry.urls')),
    path('api/v1/auth/', include('accounts.urls')),
]
