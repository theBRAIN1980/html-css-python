from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # STATUS_CHOICES = ( ('draft', 'Draft'), ('published', 'Published')
    # titles = models.CharField(max_lenght=250)
    # slug = models.SlugField(max_lenght=250, unique_for_date='publish')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts'))
    # body = models.TextField()
    # publish = models.DateTimeField(default=timezone.now)
    # created = models.DateTimeField(auto_now_add=True)
    pass

class Author(models.Model):
    pass
