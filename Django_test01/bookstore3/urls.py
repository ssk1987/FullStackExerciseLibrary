
from django.conf.urls import url,include
from django.contrib import admin
# 从当前路径导入views
from . import views

# bookstore3路由配置路由
urlpatterns = [
    url(r'^add$', views.add_view),
    url(r'^all$', views.all_view),
]
