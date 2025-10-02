from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Here i create my req and res function 

def hello(request):
    return render(request, "index.html")

# def hello(req):
#     return HttpResponse("hello morris")

def greet(req):
    return render(req, "greet.html", 
            )

def todolist(req):
    tasks = ["pray", "gym", "work"]
    return render(req, "todolist.html", {"task": tasks})

def add(req):
    if req.method == "POST":
        print(req.POST)
    return render(req, "add.html" )
    
    

