import uuid
import json

from django.db import models
from django.contrib.auth.models import AbstractUser

# Load cities from a JSON file and convert them to a tuple format
with open('fixtures/city.json') as f:
    cities = json.load(f)
cities = [(k, v) for k, v in cities.items()]


class ModelAddress(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True,
        verbose_name="Address ID", help_text="Address ID"
    )
    name = models.CharField(
        max_length=50, verbose_name="Address Title", help_text="Address Title"
    )
    city = models.CharField(
        choices=cities, max_length=20, verbose_name="City", help_text="City"
    )
    street = models.CharField(
        max_length=150, verbose_name="Street", help_text="Street"
    )
    address = models.TextField(
        max_length=500, verbose_name="Full Address", help_text="Full Address"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "Addresses"


class ModelUser(AbstractUser):
    avatar = models.ImageField(
        upload_to="Users", verbose_name="Profile Picture", help_text="Profile Picture",
        null=True, blank=True
    )
    address = models.ManyToManyField(
        ModelAddress, verbose_name="Addresses", help_text="Addresses",
        blank=True, related_name="addrs"
    )
    isCustomer = models.BooleanField(
        default=False, verbose_name="Is Customer", help_text="Is the user a customer?"
    )

    # Change the related_name for groups and user_permissions to avoid conflict with default User model
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_set', blank=True,
        verbose_name="Groups", help_text="User Groups"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions', blank=True,
        verbose_name="Permissions", help_text="User Permissions"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "Users"
