from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductCreateView,
    ContactsFormView,
    ProductListView,
    ProductDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("home/", ProductListView.as_view(), name="home"),
    path("order/<int:pk>/", ProductDetailView.as_view(), name="order"),
    path("add_product/", ProductCreateView.as_view(), name="add_product"),
]
