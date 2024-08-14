from django.shortcuts import render
from django.http import *

# Create your views here.

def page1(request):
    return HttpResponse("Page 1")


def page2(request):
    return HttpResponse("Page 2")


def page3(request):
    return HttpResponse("Page 3")

def index(request):
    return HttpResponse("This Works!")