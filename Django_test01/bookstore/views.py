from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F,Q
from . import models
# bookstore/views.py

def add_view(request):
    # 第一种插入方法
    try:
        abook = models.Book.objects.create(
            title = 'C++',
            price = 68,
            pub = '清华大学出版社',
            market_price = 75
        )
        return HttpResponse('添加成功')
    except Exception as e:
        return HttpResponse('添加失败')

def add2_view(request):
    # 第二种插入方法
    try:
        abook = models.Book(price=98)
        abook.title = '西游记'
        abook.pub = '清华大学出版社'
        abook.market_price = 108
        abook.save()
        return HttpResponse('添加成功')
    except Exception as e:
        return HttpResponse('添加失败')

# 加了模板的添加图书
def add3_view(request):
    if request.method =='GET':
        return render(request,'book/add.html')
    elif request.method =='POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price','0'))
        market_price = float(request.POST.get('market_price','0'))
        # 创建对象
        try:
            models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=market_price
            )
            # return HttpResponse('添加成功')
            return HttpResponseRedirect('/bookstore/show')
        except Exception as e:
            return HttpResponse('添加失败')
        # return render(request,'book/add.html',locals())



# 查询图书
def show_view(request):
    abook = models.Book.objects.all()# 一个可迭代的查询结果集
    #abook = models.Book.objects.values('title','pub')# 一个可迭代的查询结果集

    print(abook)
    for book in abook:
        print("书名：",book.title,"出版社：",book.pub)
    return render(request,'book/show.html',locals())

# 更新数据
def update1_view(request):
    #say = '每条记录零售价都增加10元'
    #abook = models.Book.objects.all().update(market_price=F('market_price') - 10)
    # 零售价 大于或者小于定价的书籍  __gt 大于   __lt 小于
    #say = '对数据库中两个字段的值进行比较，列出哪儿些书的零售价低于定价?'
    #abook = models.Book.objects.filter(market_price__lt= F('price'))
    # for book in abook:
    #     print(book.title,'定价:',book.price,'零售价:',book.market_price)

    say = '找定价低于50元 且 不是清华大学出版社的书籍'
    abook = models.Book.objects.filter(Q(price__lt=50) &~ Q(pub='清华大学出版社'))
    #
    # return HttpResponse('ok')
    return render(request, 'book/show.html', locals())
    # return HttpResponseRedirect('/bookstore/show')

# 编辑图书
def mod_view(request,id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception as e:
        return HttpResponse('没有id为' + id + '的数据记录')

    if request.method == 'GET':
        return render(request, 'book/mod.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price', '0'))
        market_price = float(request.POST.get('market_price', '0'))
        # 修改字段值操作
        try:
            abook.title = title
            abook.pub = pub
            abook.price = price
            abook.market_price = market_price
            abook.save()
            return HttpResponseRedirect('/bookstore/show')
        except Exception as e:
            return HttpResponse('添加失败')
# 删除图书
def del_view(request,id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception as e:
        return HttpResponse('删除失败')
    # 删除记录
    abook.delete()
    return HttpResponseRedirect('/bookstore/show')