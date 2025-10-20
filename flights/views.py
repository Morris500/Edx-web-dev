from django.shortcuts import render

from .models import flight

# Create your views here.
def index(req):
    return render (req, "index.html", {"flight": flight.objects.all()
    
    }) 