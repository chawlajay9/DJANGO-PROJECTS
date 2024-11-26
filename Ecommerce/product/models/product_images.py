from django.db import models
from .product import Product


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="product/images")

    @staticmethod
    def get_product_image(product_id, All=False):
        try:
            if All:
                return ProductImages.objects.filter(product=product_id)
            else:
                return ProductImages.objects.filter(product=product_id)[0]
        except:
            return "No images"
