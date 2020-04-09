from django.db import models


# 操作数据
class Book(models.Model):
    title = models.CharField(max_length=50, default='', verbose_name='书名')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='定价')
    # pub_date = models.DateField(default='1988-10-31')
    pub = models.CharField(max_length=50, default='', verbose_name='出版社')
    market_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='零售价')

    # author =
    # 重新定义表名称(不定义则生成 bookstore_book)
    class Meta():
        db_table = 'book'

    def __str__(self):
        return '书名： ' + self.title


class Author(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name='作者')
    age = models.IntegerField(null=False, default=1, verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='邮箱',default='xx@hx.cn')

    def __str__(self):
        return ('作者： ' + self.name + ' 年龄： ' + str(self.age) + ' 邮箱： ' + self.email)

    class Meta():
        db_table = 'author'


class Wife(models.Model):
    name = models.CharField(max_length=50, verbose_name='作家妻子')
    # 增加一对一属性
    author = models.OneToOneField(Author)

    class Meta():
        db_table = 'wife'
