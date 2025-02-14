from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=100,default="")
    body=models.TextField(default="")
class Item(models.Model):
    name=models.CharField(max_length=100,default="")
    body=models.TextField(default="")
    category = models.CharField(max_length=100, default="")