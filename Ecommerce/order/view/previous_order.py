from django.views import View
from django.shortcuts import redirect, render

from product.models.product import Product
from customer.models.customer import Customer
from ..models.order import Orders
from ..models.order_product import OrderProduct


class PreviousOrder(View):
    def get(self, request):
        customer_id = request.session.get("customerid", False)
        customer = Customer.get_customer_by_id(customer_id)
        print(customer_id)
        customer_order = Orders.get_order_by_customer(int(customer_id))
        print(f"customer_order:{customer_order}")
        customer_ordered_products = OrderProduct.get_order_product(
            customer_order)
        print(f"customer_ordered_products:{customer_ordered_products}")
        products = []
        for customer_ordered_product in customer_ordered_products:
            product_id = customer_ordered_product.product
            print(f"product_id:{type(product_id)}")
            product = Product.get_product_by_id(product_id)
            products.append(product)
        data = {}
        print(f"products Array:{products}")
        data["products"] = products
        return render(request, "previous_order.html", data)

    def post(self, request):
        pass
