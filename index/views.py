from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Here i create my req and res function 

def index(req):
    return HttpResponse("hello world")

def hello(req):
    return HttpResponse("hello morris")

def greet(req, name):
    return HttpResponse(f"hello {name}")