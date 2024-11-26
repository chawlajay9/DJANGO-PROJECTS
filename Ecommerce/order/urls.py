from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .view.cart import Cart, cart_product
from .view.checkout import Checkout
from .view.order import Order
from .view.previous_order import PreviousOrder
urlpatterns = [
    path("cart", Cart.as_view()),
    path("cartproduct", cart_product),
    path("checkout", Checkout.as_view()),
    path("order", Order.as_view()),
    path("previousorder", PreviousOrder.as_view())
]
