from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index_view(request):
    html = '<h1>Index</h1>'
    return HttpResponse(html)


def page1_view(request):
    html = '<h1>page1</h1>'
    return HttpResponse(html)


def pagen_view(request, n):
    html = 'page%s' % n
    return HttpResponse(html)


def add_view(request, a, b):
    a = int(a)
    b = int(b)
    html = '%s + %s = %s' % (a, b, a + b)
    return HttpResponse(html)


def math_view(request, x, op, y):
    # x,y从url上获取的是字符串,需要转换成Int
    x = int(x)
    y = int(y)
    result = None
    if op == 'add':
        result = '%s + %s = %s' % (x, y, x + y)
    elif op == 'sub':
        result = '%s - %s = %s' % (x, y, x - y)
    elif op == 'mul':
        result = '%s * %s = %s' % (x, y, x * y)
    if result is None:
        # return HttpResponse('出错啦')
        return HttpResponseRedirect('https://www.python87.com')
    html = "你的IP是:" + request.META['REMOTE_ADDR']
    html += '  ' + result
    return HttpResponse(html)


# def person_view(request,**kwags):
#     s = str(kwags)
#     return HttpResponse(s)
#
# {'name': 'weimz', 'age': '22'}

def person_view(request, name=None, age=None):
    s = '姓名:' + name
    s += '年龄' + age
    return HttpResponse(s)


# 姓名:weimz年龄22


# def person_view(request,name,age):
#     html = '姓名:%s - Age:%s' % (name.age)
#     return HttpResponse(html)

def birthday_view(request, y, m, d):
    html = "生日" + y + '年' + m + '月' + d + '日'
    return HttpResponse(html)


def birthday_view2(request, m, d, y):
    html = "生日" + y + '年' + m + '月' + d + '日'
    return HttpResponse(html)


def birthday_view3(request, y, m, d):
    html = "生日" + y + '年' + m + '月' + d + '日'
    return HttpResponse(html)


def mypage_view(request):
    # http://127.0.0.1:8000/mypage?a=100&b=200
    if request.method == 'GET':
        # a = request.GET['a']
        # a = request.GET.get('a','没有对应值')
        # b = request.GET['b']
        # html = a
        # html += b
        # html = str(dict(request.GET)) # {'a': ['100'], 'b': ['200', '600'], 'c': ['500']}
        a = request.GET.getlist('a')
        b = request.GET.getlist('b')
        html = 'a = ' + str(a)
        html += '  b = ' + str(b)
        return HttpResponse(html)
        # a = ['100'] b = ['200', '600']
    else:
        return HttpResponse('不是GET')


def sum_view(request):
    # sum(range(start, stop, step))
    if request.method == 'GET':
        try:
            start = int(request.GET.get('start', '0'))
            step = int(request.GET.get('step', '1'))
            stop = int(request.GET['stop'])
            result = sum(range(start, stop, step))
            return HttpResponse(str(result))
        except Exception as error:
            return HttpResponse('无效的查询字符串')


login_form_html = '''
<form method='post' action="/login">
姓名:<input type="text" name="username"><br/>
密码:<input type="password" name="pwd"><br/>
<input type='submit' value='登陆'>
</form>
'''


def login_view(request):
    if request.method == 'GET':
        return HttpResponse(login_form_html)
    elif request.method == 'POST':
        # name = request.POST['name']
        name = request.POST.get('username', '属性错误')
        html = '名称为：' + name
        s = str(dict(request.POST))
        html += s
        return HttpResponse(html)


# 名称为：ssk
# {'username': ['ssk'], 'pwd': ['aaaaaa']}

def login2_view(request):
    # 返回模板生成的html给浏览器
    # 方法一
    # 1 先加载模块
    from django.template import loader
    t = loader.get_template('mylogin.html')
    # 2 用模板生成html
    html = t.render({'name': 'python87'})
    # 3 将html返回给浏览器
    return HttpResponse(html)


def login3_view(request):
    return render(request, 'mylogin.html', {'name': 'py87.cn'})


def say_hello():
    return '您好'


class Dog():
    def say(self):
        return '旺旺'


def test_view(request):
    s = 'hello py87.cn1'
    lst = ['南京', '上海', '北京']
    mydic = {
        'name': 'ssk',
        'age': 25
    }
    dic = {
        's': s,
        'lst': lst,
        'mydic': mydic,
        'say_hello': say_hello,
        'dog1': Dog()
    }
    return render(request, 'test.html', locals())


def mytemp_view(request):
    dic = {
        'x': -5
    }
    return render(request, 'mytemp.html', dic)


def mycal_view(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        x = int(request.POST.get('x', '0'))
        y = int(request.POST.get('y', '0'))
        op = request.POST.get('op')
        result = None
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'mycal.html', locals())


def myfor_view(request):
    lst = ['南京', '上海', '北京', '广州', '深圳']
    s = '<h1>今天天气很好</h1>'
    n = 100
    s2 = 'aa bb cc dd ee ff gg hh ii jj kk ll mm nn'
    return render(request, 'myfor.html', locals())


def pindex_view(request):
    return render(request, 'pindex.html')


def sport_view(request):
    return render(request, 'sport.html')


def news_view(request):
    return render(request, 'news.html')


def pinfo_view(request):
    return render(request, 'pindex.html')


# 社保计算
def shebao_view(request):
    if request.method == 'GET':
        return render(request, 'shebao.html')
    elif request.method == 'POST':
        base = float(request.POST.get('base','0'))
        city = request.POST.get('city','1')
        # 养老
        yl_gr = base * 0.08
        yl_dw = base * 0.19
        # 失业
        sy_dw = base * 0.008
        # 城市农村
        if city == '1':
            sy_gr = base * 0.002
        else:
            sy_gr = 0
        # 工伤
        gs_gr = 0
        gs_dw = base * 0.005
        # 生育
        shengy_gr = 0
        shengy_dw = base * 0.008
        # 医疗
        yil_gr = base * 0.02 + 3
        yil_dw = base * 0.1
        # 公积金
        gjj_gr = base * 0.12
        gjj_dw = base * 0.12
        gr_result = yl_gr + sy_gr + yil_gr + shengy_gr + yil_gr + gjj_gr
        dw_result = yl_dw + sy_dw + yil_dw + shengy_dw + yil_dw + gjj_dw + gs_dw + shengy_dw
        # 纳入国家
        result = gr_result + dw_result
        return render(request, 'results_shebao.html', locals())
