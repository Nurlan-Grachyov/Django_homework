import json

from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.management.commands.comm_from_term import create_fixture
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_meat = Category.objects.create(name="meat", description="meat")
        category_instruments = Category.objects.create(
            name="instruments", description="instruments for garden"
        )
        product_meat = Product.objects.create(
            name="beef",
            description="delicious beef",
            category=category_meat,
            price=300,
            created_at="2025-01-06",
            updated_at="2025-01-06",
        )
        product_instruments = Product.objects.create(
            name="shovel",
            description="iron shovel",
            category=category_instruments,
            price=500,
            created_at="2025-01-06",
            updated_at="2025-01-06",
        )

        create_fixture()
        fixture_path = "new_fixture_utf8.json"
        call_command("loaddata", fixture_path)
