# Generated by Django 5.1.5 on 2025-01-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="order/photo",
                verbose_name="изображение",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now=True, verbose_name="дата последнего изменения"
            ),
        ),
    ]
