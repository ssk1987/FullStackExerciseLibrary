from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def add_view(request):
    pass


def all_view(request):
    authors = models.Author3.objects.all()

    for auth in authors:
        print('作者：', auth.name, ' 出版了：', auth.book3_set.count(), '本书：')
        # 通过 作者 查询对应的所有的书籍
        books = auth.book3_set.all()
        for book in books:
            print('    ', book.title)

    print('---------显示书和作者的关系-----------')
    books = models.Book3.objects.all()
    for book in books:
        auths = book.author.all()
        print(book.title, '的作者是:', '、'.join([str(x.name) for x in auths]))
    return HttpResponse('显示成功,请查看控制台')
