from django.db import models
from .category import Category


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return SubCategory.objects.all()
