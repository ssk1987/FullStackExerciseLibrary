"""Django_test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# 从当前路径导入views
from . import views

# 主路由配置路由
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_view),
    url(r'^page1', views.page1_view),
    url(r'^mypage', views.mypage_view),
    url(r'^page(\d+)', views.pagen_view),
    # url(r'^(\d+)/add/(\d+)$', views.add_view),
    url(r'^(\d+)/(\w{3})/(\d+)$', views.math_view),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})', views.person_view),
    # url(r'^birthday/(\d{4})/(\d{1,2})/(\d{1,2})', views.birthday_view),
    # url(r'^birthday/(\d{1,2})/(\d{1,2})/(\d{4})', views.birthday_view2),
    url(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})', views.birthday_view3),
    url(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})', views.birthday_view3),
    url(r'^sum', views.sum_view),
    url(r'^login$', views.login_view),
    url(r'^login2$', views.login2_view),
    url(r'^login3$', views.login3_view),
    url(r'^test$', views.test_view),
    url(r'^mytemp$', views.mytemp_view),
    url(r'^mycal$', views.mycal_view),
    url(r'^myfor$', views.myfor_view),
    url(r'^pindex$', views.pindex_view,name='pindex'),
    url(r'^sport$', views.sport_view,name='sport'),
    url(r'^news$', views.news_view,name='news'),
    url(r'^pinfo(\d+)', views.pinfo_view,name='pinfo'),
    url(r'^shebao$', views.shebao_view,name='shebao'),
    # 分布式路由（子路由）
    url(r'^music/', include('music.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^sport/', include('sport.urls')),
    url(r'^bookstore/', include('bookstore.urls')),
    url(r'^bookstore2/', include('bookstore2.urls')),
    url(r'^bookstore3/', include('bookstore3.urls')),
]
