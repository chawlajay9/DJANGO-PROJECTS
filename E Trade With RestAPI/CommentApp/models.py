import uuid
from django.db import models
from UserApp.models import ModelUser
from ProductsApp.models import ModelProduct
from django.utils.encoding import smart_str


class ModelComment(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
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
    comment = models.TextField(
        max_length=300,
        verbose_name="Comment",
        help_text="Comment"
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
        help_text="Creation Date"
    )
    modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Modification Date",
        help_text="Modification Date"
    )

    def __str__(self):
        return smart_str(f"{self.user} | {self.comment}")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "Comments"
