from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from unidecode import unidecode

from SellerApp.models import ModelSeller

# Create your models here.
class BaseProductModel(models.Model):
    # Created a base class to avoid code duplication
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name", unique=True, help_text="Slug", verbose_name="Slug")

    class Meta:
        abstract = True


class ModelProductCategory(BaseProductModel):
    # The two fields (name and slug) come from the inherited (BaseProductModel) class.
    slug = AutoSlugField(populate_from="name", unique=True, help_text="Slug", verbose_name="Slug", primary_key=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nameField = self._meta.get_field('name')
        nameField.verbose_name = 'Category Name'
        nameField.help_text    = "Category Name"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Product Category"
        verbose_name_plural = "Product Categories"
        db_table            = "ProductCategories"


class ModelProduct(BaseProductModel):
    # The two fields (name and slug) come from the inherited (BaseProductModel) class.
    description = models.TextField(max_length=500, verbose_name="Description", help_text="Description")
    category    = models.ManyToManyField(
        ModelProductCategory,
        verbose_name="Category",
        help_text="Category",
        related_name="categs",
    )
    image    = models.ImageField(upload_to="Products", verbose_name="Image", help_text="Image", blank=True, null=True)
    draft    = models.BooleanField(default=True, verbose_name="Draft", help_text="Draft")
    price    = models.FloatField(verbose_name="Price", help_text="Price")
    seller   = models.ForeignKey(ModelSeller, on_delete=models.CASCADE, verbose_name="Store", help_text="Store", related_name="products")
    shipping = models.BooleanField(default=True, verbose_name="Shipping", help_text="Shipping")

    def __str__(self):
        return f"{self.name} | {self.slug}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(ModelProduct, self).save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nameField = self._meta.get_field('name')
        nameField.verbose_name = 'Product Name'
        nameField.help_text    = "Product Name"

    class Meta:
        verbose_name        = "Product"
        verbose_name_plural = "Products"
        db_table            = "Products"
