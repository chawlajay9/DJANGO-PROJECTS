from django.views import View
from django.shortcuts import render

from product.models.subcategory import SubCategory
from product.models.product import Product


class Store(View):
    def get(self, request):
        sub_category = request.GET.get("subcategory")
        products = Product.get_all_products_by_sub_category(sub_category)
        sub_categories = SubCategory.get_all_categories()
        data = {}
        data['sub_categories'] = sub_categories
        data['products'] = products
        return render(request, "store.html", data)

    def post(self, request):
        pass
