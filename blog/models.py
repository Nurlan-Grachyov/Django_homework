from django.db import models
from django.db.models import (
    CharField,
    TextField,
    ImageField,
    DateField,
    BooleanField,
    IntegerField,
)


class Blog(models.Model):
    name = CharField(max_length=100, verbose_name="заголовок")
    description = TextField(verbose_name="содержимое")
    image = ImageField(
        verbose_name="изображение", null=True, blank=True, upload_to="blog/photo"
    )
    created_at = DateField(verbose_name="дата создания", auto_now_add=True)
    is_created = BooleanField(default=True)
    viewing = IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["name", "created_at", "is_created", "viewing"]

    def __str__(self):
        return self.name
