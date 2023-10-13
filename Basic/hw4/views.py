from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ProductFormWidget, ProductChoiceForm
from hw2.models import Product

from django.shortcuts import redirect


def product_update_form(request, product_id):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            # Делаем что-то с данными
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            count = form.cleaned_data.get('count')

            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product.objects.filter(pk=product_id).first()
            product.product_name = name
            product.product_price = price
            product.product_description = description
            product.product_count = count
            product.image = image.name

            product.save()

    else:
        form = ProductFormWidget()
    return render(request, 'hw4/product_update.html', {'form': form})


def product_update_id_form(request):
    if request.method == 'POST':
        form = ProductChoiceForm(request.POST)
        if form.is_valid():
            prod_id = form.cleaned_data.get('product_id')  # получил id продукта - номер из выпадающего списка
            response = redirect(f'/hw4/product_update/{prod_id}')
            return response
    else:
        form = ProductChoiceForm()
    return render(request, 'hw4/product_update_id.html', {'form': form})


def index(request):
    return render(request, 'hw4/index.html')
