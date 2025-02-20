from django.contrib import admin
from .models import Post,Item,Author,Book
from django.urls import reverse
# Register your models here.
@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ('pk','title','category')
    search_fields = ('title',)
    list_filter = ('category',)

@admin.register(Item)
class ItemsModel(admin.ModelAdmin):
    list_display = ('pk','name', 'category')

@admin.register(Author)
class AuthorModel(admin.ModelAdmin):
    list_display = ('pk','name')

@admin.register(Book)
class BookModel(admin.ModelAdmin):
    list_display = ('pk','author_name','title')



