# Generated by Django 5.1.4 on 2024-12-10 13:07

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ModelSeller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "companyName",
                    models.CharField(
                        help_text="Company Name",
                        max_length=150,
                        null=True,
                        verbose_name="Company Name",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        help_text="Phone",
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Phone",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        help_text="Website",
                        max_length=300,
                        null=True,
                        verbose_name="Website",
                    ),
                ),
            ],
            options={
                "verbose_name": "Seller",
                "verbose_name_plural": "Sellers",
                "db_table": "Sellers",
            },
        ),
    ]
