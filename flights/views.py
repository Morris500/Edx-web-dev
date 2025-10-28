from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Passenger, flight

# Create your views here.
def index(req):
    return render (req, "index.html", {"flights": flight.objects.all()
     
    }) 

def flight_detail(req, flight_id):
    flight_obj = flight.objects.get(pk=flight_id)
    
    return render (req, "flight.html", 
                   {
                       "flights": flight_obj, 
                       "passengers":flight_obj.passengers.all(), 
                       "non_passengers": Passenger.objects.exclude(flights=flight_obj).all()
                       } )


def book(req, flight_id):
    if req.method == "POST":
        flight_book = flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(req.POST["passenger"]))
        passenger.flights.add(flight_book)

        return HttpResponseRedirect(reverse("flight", args=(flight_book.id)))
