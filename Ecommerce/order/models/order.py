from django.db import models

from customer.models.customer import Customer
from customer.models.address import Address


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)

    def save_order(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        try:
            return Orders.objects.get(customer=customer_id)
        except:
            return False
