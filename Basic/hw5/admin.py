from django.contrib import admin
from hw2.models import Product, Order, Client


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""

    list_display = ['product_name', 'product_price', 'product_count']
    ordering = ['product_name', '-product_count']
    list_filter = ['product_price']
    search_fields = ['product_description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""

    fields = ['product_name', 'product_description', 'product_price', 'product_count']
    readonly_fields = ['product_name']


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['user_name', 'user_mail', 'user_phone_number', 'user_adres', 'registration_date']
    ordering = ['user_name']
    list_filter = ['user_name']
    search_fields = ['user_name']
    search_help_text = 'Поиск по полю Имя клиента (user_name)'

    """Отдельный клиент"""
    fields = ['user_name', 'user_mail', 'user_phone_number', 'user_adres', 'registration_date']
    readonly_fields = ['user_name', 'registration_date']


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""

    def _products(self, row):
        return ','.join([x.product_name for x in row.products.all()])


    def _client(self, row):
        return row.client.user_name

    list_display = ['_client', '_products', 'summa', 'order_date']
    ordering = ['client', 'summa', '-order_date']
    list_filter = ['summa']
    search_fields = ['client', 'date_ordered']

    """Отдельный заказ"""

    fields = ['client', 'products', 'summa', 'order_date']
    readonly_fields = ['order_date']

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
