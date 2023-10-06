from django.core.management.base import BaseCommand
from hw2.models import Order, Client, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('-p', '--product_id', nargs='+', help='Client ID', required=True)

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('pk')
        product_id: list = kwargs.get('product_id')

        client = Client.objects.filter(pk=client_id).first()

        order = Order(client=client)
        summ = 0
        for i in range(0, len(product_id)):
            product = Product.objects.filter(pk=product_id[i]).first()
            summ += float(product.product_price)
            order.summa = summ
            order.save()
            order.products.add(product)
