from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from rest_framework import generics
from ..models import Product
from .serializers import ProductSerializer


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category_name = ''
    if category_slug:
        category_name = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_name)
    return render(request, 'list.html', {'products': products,
                                    'category': category_name,
                                    'categories': categories})

def product_detail(request, slug):
    produs = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/products/detail.html', {'product': produs})

class ProductlistView(generic.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

