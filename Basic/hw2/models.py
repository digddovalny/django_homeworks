from django.db import models


# Create your models here.


class Client(models.Model):
    user_name = models.CharField(max_length=100)
    user_mail = models.EmailField()
    user_phone_number = models.CharField(max_length=12)
    user_adres = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.user_name} , email: {self.user_mail}, phone: {self.user_phone_number},' \
               f' adres_of_client: {self.user_adres}, date: {self.registration_date}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
    product_add_date = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to='images')

    def __str__(self):
        return f' name: {self.product_name}, descr: {self.product_description},' \
               f' price: {self.product_price}, quantity: {self.product_count}'


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    summa = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Клиент: {self.client},' \
               f' сумма заказа {self.summa},' \
               f' товары {self.products},' \
               f' дата заказа {self.order_date}'
