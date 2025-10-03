from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here. Here i create my req and res function 

def hello(request):
    return render(request, "index.html")

# def hello(req):
#     return HttpResponse("hello morris")

def greet(req):
    return render(req, "greet.html", 
            )
tasks = ["pray", "gym", "work"]

def todolist(req):
    return render(req, "todolist.html", {"task": tasks})

def add(req):
    if req.method == "POST":
        data =  req.POST.get('task')
        tasks.append(data)
        return HttpResponseRedirect(reverse("todolist"))
    else:
        return render(req, "add.html" )
    

    
    

