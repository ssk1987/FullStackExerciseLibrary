from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name='出版社')

    def __str__(self):
        return '出版社' + self.name

    class Meta():
        db_table = 'publisher'


class Book2(models.Model):
    title = models.CharField(max_length=30, verbose_name='书名')
    pub = models.ForeignKey(Publisher, null=True)

    def __str__(self):
        return '书名2' + self.title
    class Mete():
        db_table = 'book2'
