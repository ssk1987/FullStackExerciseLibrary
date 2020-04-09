from django.http import HttpResponse
from django.shortcuts import render


# music/views.py

def page1_view(request):
    return HttpResponse('页面1')


def page2_view(request):
    return HttpResponse('页面1')


def page3_view(request):
    return HttpResponse('页面1')
