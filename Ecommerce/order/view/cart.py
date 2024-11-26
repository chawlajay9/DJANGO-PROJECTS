from django.views import View
from django.shortcuts import redirect, render

from product.models.product import Product


class Cart(View):
    def get(self, request):
        pass

    def post(self, request):
        is_customer_login = request.session.get("customerid", False)
        if is_customer_login:
            cart_product = request.POST.get("cartproduct")
            page = request.POST.get("page")
            add_product = request.POST.get("add")
            remove_product = request.POST.get("remove")
            cart = request.session.get('cart', False)
            if cart:
                product_quantity = cart.get(cart_product)
                if product_quantity:
                    if add_product:
                        cart[cart_product] = product_quantity + 1
                    elif remove_product:
                        cart[cart_product] = product_quantity - 1
                else:
                    cart[cart_product] = 1
            else:
                cart = {}
                cart[cart_product] = 1
            request.session['cart'] = cart
            return redirect(page)
        else:
            return redirect('/login')


def cart_product(request):
    cart = request.session.get("cart", False)
    product_ids = cart.keys()
    products = []
    for product_id in product_ids:
        product = Product.get_product_by_id(product_id)
        products.append(product)
    data = {}
    data['products'] = products
    print(f"product:{products}")
    return render(request, "cart.html", data)
