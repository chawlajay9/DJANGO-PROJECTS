from typing import Container
from django.contrib import admin
# Register your models here.
from .models.product import Product
from .models.category import Category
from .models.subcategory import SubCategory
from .models.product_images import ProductImages


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminSubCategory(admin.ModelAdmin):
    list_display = ['category', 'name']


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'sub_category']


class AdminProductImages(admin.ModelAdmin):
    list_display = ['product', 'image']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(SubCategory, AdminSubCategory)
admin.site.register(ProductImages, AdminProductImages)
