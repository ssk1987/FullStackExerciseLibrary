from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F,Q
from . import models

def add_view(request):
    try:
        pub1 = models.Publisher.objects.create(name='清华大学出版社')
        models.Book2.objects.create(title='C++',pub=pub1)
        models.Book2.objects.create(title='Java',pub=pub1)
        models.Book2.objects.create(title='Pyhon3',pub=pub1)

        pub2 = models.Publisher.objects.create(name='北京大学出版社')
        models.Book2.objects.create(title='西游记',pub=pub2)
        models.Book2.objects.create(title='水浒传',pub=pub2)
        return HttpResponse('添加成功')
    except Exception as e:
        return HttpResponse('添加失败')












