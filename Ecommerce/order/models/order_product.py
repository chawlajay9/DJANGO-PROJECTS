from django.db import models

from product.models.product import Product
from .order import Orders


class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def save_order_product(self):
        self.save()

    @staticmethod
    def get_order_product(order_product_id):
        try:
            return OrderProduct.objects.filter(id=order_product_id)
        except:
            return False
