from django.contrib import admin
from .models import Post,Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'author', 'created_on']
    search_fields = ['title', 'author', 'slug']
    list_filter = ['title', 'author', 'tags']

@admin.register(Tag)
class TagtAdmin(admin.ModelAdmin):
    list_display =['id', 'name']
    search_fields = ['title']