from django.db import models
from UserApp.models import ModelUser
from phonenumber_field.modelfields import PhoneNumberField


class ModelSeller(models.Model):
    user        = models.ForeignKey(ModelUser, on_delete=models.CASCADE, verbose_name="User", help_text="User")
    companyName = models.CharField(max_length=150, verbose_name="Company Name", help_text="Company Name", null=True)
    phone       = PhoneNumberField(help_text="Phone", verbose_name="Phone", null=True)
    website     = models.URLField(max_length=300, verbose_name="Website", help_text="Website", null=True, blank=True)

    def __str__(self):
        return f"{self.companyName}"

    class Meta:
        verbose_name        = "Seller"
        verbose_name_plural = "Sellers"
        db_table            = "Sellers"
