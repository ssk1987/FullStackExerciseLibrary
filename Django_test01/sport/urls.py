from django.conf.urls import url
from . import views
# music/urls.py
urlpatterns = [
    url(r'^index$',views.index_view),
]