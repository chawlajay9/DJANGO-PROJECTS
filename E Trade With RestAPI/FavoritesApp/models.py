from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct


class ModelFavorite(models.Model):
    user = models.ForeignKey(
        ModelUser,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="User"
    )
    product = models.ForeignKey(
        ModelProduct,
        on_delete=models.CASCADE,
        verbose_name="Product",
        help_text="Product"
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Save Date",
        help_text="Save Date"
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        db_table = "Favorites"

    def __str__(self):
        return f"{self.user.username}'s favorite is {self.product.name}"
