import uuid
from django.db import models
from UserApp.models import ModelUser, ModelAddress
from ProductsApp.models import ModelProduct


class ModelOrder(models.Model):
    user = models.ForeignKey(
        ModelUser,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="User",
        related_name="orders"
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Order Date",
        help_text="Order Date"
    )
    address = models.ForeignKey(
        ModelAddress,
        on_delete=models.SET_NULL,
        verbose_name="Address",
        help_text="Address",
        blank=False,
        null=True
    )
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Order ID",
        help_text="Order ID"
    )

    class Meta:
        db_table = "Orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.unique_id}"


class ModelOrderItems(models.Model):
    order = models.ForeignKey(
        ModelOrder,
        on_delete=models.CASCADE,
        verbose_name="Order",
        help_text="Order",
        related_name="items"
    )
    item = models.ForeignKey(
        ModelProduct,
        on_delete=models.CASCADE,
        verbose_name="Product",
        help_text="Product"
    )
    amount = models.PositiveIntegerField(
        verbose_name="Quantity",
        help_text="Quantity"
    )
    price = models.PositiveIntegerField(
        verbose_name="Price",
        help_text="Price"
    )

    def __str__(self):
        return str(self.item.name)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
        db_table = "OrderItems"
