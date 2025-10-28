from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(req):
    if not req.user.is_authenticated:
      return HttpResponseRedirect(reverse("login"))
    return render(req, "users.html")

def login_view(req):
    if req.method == "POST":
        username=req.POST['username']
        password=req.POST['password']
        user = authenticate(req, username= username, password=password )
        if user is not None:
            login(req, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(req, "login.html",{
                "message": "Invalid credentials."
            })
    return render(req, "login.html")
        
def logout_view(req):
    return render(req, "login.html", {"message": 'logout'})