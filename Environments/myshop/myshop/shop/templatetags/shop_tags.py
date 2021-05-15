from django import template
from ..models import Product

register = template.Library()

@register.simple_tag
def total_products():
    return Product.objects.all().count()

@register.filter
def greet(value):
    return f"Hello {name}"

@register.filter
def price(value):
    return f"{name} $"