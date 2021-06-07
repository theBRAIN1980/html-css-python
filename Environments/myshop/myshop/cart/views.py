from django.shortcuts import render
from django.http import HttpResponse


def cart_detail(request):
    return render(request, 'cart_detail.html')

def cart_add(request):
    return render(request, 'cart_add.html')

def cart_remove(request):
    return render(request, 'cart_remove.html')



