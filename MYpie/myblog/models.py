from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=100,default="")
    body=models.TextField(default="")

class Item(models.Model):
    name=models.CharField(max_length=100,default="")
    body=models.TextField(default="")
    category = models.CharField(max_length=100, default="")
class Author(models.Model):
    name=models.CharField(max_length=100,default="")
    def __str__(self):
        return(f'{self.name}')
class Book(models.Model):
    title = models.CharField(max_length=100, default="")
    body = models.TextField(default="")
    author_name=models.ForeignKey(Author,on_delete=models.CASCADE)
    slug= models.SlugField(unique=True, blank=True)
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={'slug': self.slug})

