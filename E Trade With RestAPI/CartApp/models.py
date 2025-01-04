from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct


class ModelCart(models.Model):
    user = models.ForeignKey(
        ModelUser,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="User",
        related_name="cart"
    )

    def __str__(self):
        return f"{self.user.username}'s cart."

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        db_table = "Cart"

    def get_total_price(self):
        total_price = 0
        products = self.user.cart.first().items.all()
        for product in products:
            total_price += product.product.price
        return total_price


class ModelCartItem(models.Model):
    cart = models.ForeignKey(
        ModelCart,
        on_delete=models.CASCADE,
        verbose_name="Cart",
        help_text="Cart",
        related_name="items"
    )
    product = models.ForeignKey(
        ModelProduct,
        on_delete=models.CASCADE,
        verbose_name="Product",
        help_text="Product"
    )
    amount = models.IntegerField(
        verbose_name="Quantity",
        help_text="Quantity"
    )

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        db_table = "CartItems"
