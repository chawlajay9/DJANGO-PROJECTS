from django.views import View
from django.shortcuts import redirect, render

from product.models.product import Product


class Checkout(View):
    def get(self, request):
        cart = request.session.get("cart", False)
        products = []
        total = 0
        for product_id, count in cart.items():
            product = Product.get_product_by_id(product_id)
            total += int(product.price) * int(count)
            products.append(product)
        data = {}
        data["products"] = products
        data["total"] = total
        return render(request, "checkout.html", data)

    def post(self, request):
        pass
