
'''
此模块实现music 应用中的子路由配置
'''
from django.conf.urls import url
from . import views
# music/urls.py
urlpatterns = [
    url(r'^page1$',views.page1_view),
]