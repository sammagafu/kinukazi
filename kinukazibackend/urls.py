from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/machine/', include('product.urls')),
    path('api/v1/category/', include('industry.urls')),
    path('api/v1/auth/', include('accounts.urls')),
    # path('api/v1/auth/', include('djoser.urls')),x
    # url(r'^auth/', include('djoser.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
