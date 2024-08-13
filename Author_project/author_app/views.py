from django.shortcuts import render
from django.http import *
from .models import Author
# Create your views here.

def index(request):
    listsss=Author.objects.all()
    return render(request,"authors/authors.html",{"author":listsss})