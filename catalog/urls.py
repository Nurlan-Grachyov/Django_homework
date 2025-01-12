from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, home, order

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name='contacts'),
    path("home/", home, name='home'),
    path("order/<int:pk>/", order, name='order'),
]
