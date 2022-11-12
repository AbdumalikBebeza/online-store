from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Product


def main(request):
    if request.method == 'GET':
        products = Product.objects.all()

        data = {
            'products': products
        }
        return render(request, 'layouts/main.html', context=data)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)
