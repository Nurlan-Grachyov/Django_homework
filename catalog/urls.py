from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, order, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("home/", home, name="home"),
    path("order/<int:pk>/", order, name="order"),
    path("add_product/", add_product, name="add_product"),
]
