from django.views import View
from django.shortcuts import render

from product.models.product_images import ProductImages
from product.models.product import Product


class ProductDetail(View):
    def get(self, request):
        product_id = request.GET.get("productid")
        product = Product.get_product_by_id(product_id)
        product_images = ProductImages.get_product_image(product_id, All=True)
        data = {}
        data['product'] = product
        data['product_images'] = product_images
        data['product_main_preview_image'] = product_images[0]
        return render(request, "product.html", data)

    def post(self, request):
        pass
