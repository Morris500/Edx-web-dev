from django.shortcuts import render

from .models import flight

# Create your views here.
def index(req):
    return render (req, "index.html", {"flights": flight.objects.all()
     
    }) 

def Flight(req, flight_id):
    Flight = flight.objects.get(pk=flight_id)
    print(Flight)
    return render (req, "flight.html", {"flights": Flight } )
