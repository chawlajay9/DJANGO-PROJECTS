from django import template

from product.models.product_images import ProductImages

register = template.Library()


@register.filter(name="get_image")
def get_image(product_id):
    product_images = ProductImages.get_product_image(product_id)
    product_image_url = product_images.image.url
    return product_image_url
