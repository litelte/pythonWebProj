# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """调用index方法的话，就会通过web的方式返回Hello world"""

    return HttpResponse("Hello world")
