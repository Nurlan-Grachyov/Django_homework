from django.db import models
from django.db.models import (
    CharField,
    TextField,
    ImageField,
    IntegerField,
    DateField,
    ForeignKey,
)


class Product(models.Model):
    name = CharField(max_length=100, verbose_name="наименование")
    description = TextField(verbose_name="описание")
    image = ImageField(
        verbose_name="изображение", null=True, blank=True, upload_to="order/photo"
    )
    category = ForeignKey(
        "Category", verbose_name="категория", on_delete=models.CASCADE
    )
    price = IntegerField(verbose_name="цена за покупку")
    created_at = DateField(verbose_name="дата создания")
    updated_at = DateField(verbose_name="дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = CharField(max_length=100, verbose_name="наименование")
    description = TextField(verbose_name="описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
