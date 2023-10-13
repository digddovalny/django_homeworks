from django.db import models


# Create your models here.


class Client(models.Model):
    user_name = models.CharField(max_length=100)
    user_mail = models.EmailField()
    user_phone_number = models.CharField(max_length=12)
    user_adres = models.TextField()
    registration_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
    product_add_date = models.DateTimeField()
    #image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.product_name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    summa = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(default='2001-09-11T00:00:00.000Z')

    def __str__(self):
        return f'Клиент: {self.client},' \
               f' сумма заказа {self.summa},' \
               f' товары {self.products},' \
               f' дата заказа {self.order_date}'
