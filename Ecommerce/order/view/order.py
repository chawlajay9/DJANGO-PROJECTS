from django.views import View
from django.shortcuts import redirect, render

from customer.models.customer import Customer
from ..models.order import Orders
from ..models.order_product import OrderProduct
from customer.models.address import Address
from product.models.product import Product


class Order(View):
    def get(self, request):
        pass

    def post(self, request):
        address_data = request.POST
        address = address_data.get("address")
        city = address_data.get("city")
        state = address_data.get("state")
        zipcode = address_data.get("zipcode")
        country = address_data.get("country")

        customer_id = request.session.get("customerid", False)
        customer_id = int(customer_id)
        customer = Customer.get_customer_by_id(customer_id)
        customer_address = Address(
            customer=customer,
            address=address,
            city=city,
            state=state,
            zipcode=int(zipcode),
            country=country
        )
        customer_address.save_address()

        # Order Details
        orders = Orders(customer=customer, address=customer_address)
        orders.save_order()

        # Store Order product
        cart = request.session.get("cart", False)
        products = []
        if cart:
            product_ids = cart.keys()
            for product_id in product_ids:
                order_product = OrderProduct(orders.id, int(product_id))
                order_product.save_order_product()
                # To pass already purchased product at black page
                product = Product.get_product_by_id(product_id)
                products.append(product)
            del request.session['cart']

        return render(request, "previous_order.html", {"products": products})
