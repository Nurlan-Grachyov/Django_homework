from django.http import HttpResponse
from django.shortcuts import render


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def home(request):
    return render(request, "home.html")
