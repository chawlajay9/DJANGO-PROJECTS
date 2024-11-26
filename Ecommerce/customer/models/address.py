from django.db import models
from .customer import Customer


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def save_address(self):
        self.save()

    @staticmethod
    def get_address_by_customer(customer_id):
        try:
            return Address.objects.get(id=customer_id)
        except:
            return False
