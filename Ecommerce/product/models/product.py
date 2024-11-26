from django.db import models
from django.db.models.deletion import CASCADE

from .subcategory import SubCategory


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    sub_category = models.ForeignKey(SubCategory, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products_by_sub_category(sub_category):
        if sub_category:
            return Product.objects.filter(sub_category=sub_category)
        else:
            return Product.objects.all()

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except:
            return Product.objects.get(id=1)
