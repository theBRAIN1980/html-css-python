from django.db import models

class Category(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category.__name__, related_name="products", on_delete=models.CASCADE) 
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to="static/images/products%Y%m%d")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    search_fields = ('name', 'category__name')
    list_editable = ['price', 'available']
    def __str__(self):
        return self.name

