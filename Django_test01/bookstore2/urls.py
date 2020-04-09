
from django.conf.urls import url,include
from django.contrib import admin
# 从当前路径导入views
from . import views

# bookstore2路由配置路由
urlpatterns = [
    url(r'^add$', views.add_view),
    # url(r'^add2$', views.add2_view),
    # url(r'^add3$', views.add3_view),
    # url(r'^show$', views.show_view),
    # url(r'^mod/(\d+)', views.mod_view),
    # url(r'^del/(\d+)', views.del_view),
    # url(r'^update1$', views.update1_view),
]
