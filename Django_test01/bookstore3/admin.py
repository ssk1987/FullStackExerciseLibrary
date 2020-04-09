from django.contrib import admin

# Register your models here.
from . import models


class Author3Manager(admin.ModelAdmin):
    list_display = ['id', 'name']


class Book3Manager(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(models.Author3, Author3Manager)
admin.site.register(models.Book3, Book3Manager)
