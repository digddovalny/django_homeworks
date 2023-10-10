from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Client, Order


# Create your views here.


def hw2(request):
    return render(request, 'hw2/index.html')


def basket(request, client_id):
    products = []
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'hw2/user_all_orders.html', {'client': client, 'orders': orders, 'products': products})


def sorted_basket(request, client_id, days_ago):
    products = []
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(customer=client, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'hw2/user_all_products.html', {'client': client, 'product_set': product_set, 'days': days_ago})
