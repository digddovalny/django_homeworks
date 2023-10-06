from django.http import HttpResponse
from django.shortcuts import render

from hw2.models import Client, Product, Order


# Create your views here.


def hw2(request):
    return HttpResponse("HomeWork2")


def clients(request):
    clients = Client.objects.all()
    return HttpResponse(clients)


def products(request):
    products = Product.objects.all()
    return HttpResponse(products)


def orders(request):
    orders = Order.objects.all()
    return HttpResponse(orders)
