from django.core.management.base import BaseCommand
from hw2.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        product = Product(product_name='апельсин',
                        product_description='красный апельсик',
                        product_price=1337.22,
                        product_count=0,
                        product_add_date='1999-09-23T18:25:43.511Z')

        product.save()
        self.stdout.write(f'{product}')