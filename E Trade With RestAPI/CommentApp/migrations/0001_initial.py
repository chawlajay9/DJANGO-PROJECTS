# Generated by Django 5.1.4 on 2024-12-25 15:40

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ProductsApp", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelComment",
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
                    "unique_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Comment", max_length=300, verbose_name="Comment"
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Creation Date",
                        verbose_name="Creation Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Modification Date",
                        verbose_name="Modification Date",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Product",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ProductsApp.modelproduct",
                        verbose_name="Product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
                "db_table": "Comments",
            },
        ),
    ]
