from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Product, Review


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


def detail_view(request, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])
        reviews = Review.objects.filter(product=product)

        data = {
            'product': product,
            'reviews': reviews
        }

        return render(request, 'products/detail.html', context=data)
