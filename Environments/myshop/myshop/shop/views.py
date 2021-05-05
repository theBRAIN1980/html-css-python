from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category_name = ''
    if category_slug:
        category_name = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_name)
    return render(request, 'products/list.html', {'products': products,
                                    'category': category_name,
                                    'categories': categories})


