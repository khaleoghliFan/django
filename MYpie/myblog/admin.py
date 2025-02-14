from django.contrib import admin
from .models import Post,Item

# Register your models here.
@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ('title','category')
    search_fields = ('title',)
    list_filter = ('category',)

@admin.register(Item)
class ItemsModel(admin.ModelAdmin):
    list_display = ('name', 'category')

