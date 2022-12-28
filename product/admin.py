from django.contrib import admin
from .models import Product,ProductImage,ProductFeatures

# Register your models here.
class ProductImageInline(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(ProductFeatures)
# Register your models here.
