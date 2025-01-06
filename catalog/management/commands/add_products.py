import json

from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_fruit, _ = Category.objects.get_or_create(name='fruit')
        category_vegetables, _ = Category.objects.get_or_create(name='vegetables')

        with open('catalog_fixture.json', 'r') as json_file:
            products = json.load(json_file)

        for product_data in products:
            if product_data.get('model') == "catalog.product":
                product, created  = Product.objects.get_or_create(**product_data['fields'])
                if created:
                    self.stdout.write(f'Successfully added products: {product.name}')
                else:
                    self.stdout.write(f'products already exists: {product.name}')
