from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Create client"

    def handle(self, *args, **kwargs):
        client = Client(user_name='C',
                        user_mail='ssdsd@mail.ru',
                        user_phone_number='+11777277',
                        user_adres='MOskva',
                        registration_date='2012-09-23T18:25:43.511Z')

        client.save()
        self.stdout.write(f'{client}')