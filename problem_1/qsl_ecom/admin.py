from django.contrib import admin
from .models import Category, Brand, Warranty, Seller, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['duration']

class SellerAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'warranty', 'seller', 'price']
    list_filter = ['category', 'brand', 'warranty', 'seller']
    search_fields = ['name', 'category__name', 'brand__name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)