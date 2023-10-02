from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Магазин мебели'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)

def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item.name
    }

    return render(request, 'catalog/product.html', context)

