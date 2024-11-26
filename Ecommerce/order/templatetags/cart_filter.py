from django import template
from django.shortcuts import render

from product.models.product import Product

register = template.Library()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    product = str(product)
    is_exist = cart.get(product, False)
    if is_exist:
        return True
    else:
        return False


@register.filter(name="get_product_quantity")
def get_product_quantity(product, cart):
    product = str(product)
    quantity = cart.get(product)
    return quantity


@register.filter(name="get_cart_product_count")
def get_cart_product_count(cart):
    if cart:
        count = len(cart.keys())
        return count
    else:
        return 0


@register.filter(name="get_product_total")
def get_product_total(product_id, cart):
    if cart:
        product = Product.get_product_by_id(product_id)
        count = cart.get(str(product_id), 0)
        total = int(product.price) * int(count)
        return total
    else:
        return 0
