from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .view.product_details import ProductDetail
from .view.store import Store

urlpatterns = [
    path("product", ProductDetail.as_view()),
    path("store", Store.as_view())
]
