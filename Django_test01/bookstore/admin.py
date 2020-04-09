from django.contrib import admin

from . import models


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'market_price', 'pub']
    list_display_links = ['id', 'title']
    list_filter = ['pub']
    search_fields = ['title', 'pub']
    list_editable = ['market_price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'email']
    search_fields = ['name', 'age', 'email']
    list_editable = ['age', 'email']

class WifeManager(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


# admin.site.register(models.Book)
admin.site.register(models.Book, BookManager)
admin.site.register(models.Author, AuthorManager)
admin.site.register(models.Wife,WifeManager)
