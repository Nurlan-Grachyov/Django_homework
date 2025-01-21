from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView

from catalog.forms import ContactForm
from catalog.models import Product


class ContactsFormView(FormView):
    template_name = "contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("contacts")


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "orders"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "order"


class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    fields = [
        "name",
        "category",
        "description",
        "price",
        "image",
    ]
    success_url = reverse_lazy("catalog:home")
