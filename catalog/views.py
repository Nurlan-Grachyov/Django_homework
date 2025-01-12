from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def home(request):
    orders = Product.objects.all()
    context = {
        'orders': orders
    }
    return render(request, "home.html", context=context)


def order(request, pk):
    order_db = Product.objects.get(pk=pk)
    context = {
        'order': order_db
    }
    return render(request, "order.html", context=context)
