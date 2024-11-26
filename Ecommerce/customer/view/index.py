from django.views import View
from django.shortcuts import render

from product.models.subcategory import SubCategory
from product.models.product import Product


class Index(View):
    def get(self, request):
        data = {}
        products = Product.get_all_products()
        data['products'] = products
        sub_categories = SubCategory.get_all_categories()
        data['sub_categories'] = sub_categories
        return render(request, "index.html", data)

    def post(self, request):
        pass
