from django.shortcuts import render
import datetime

# Create your views here.

def newyear(req):
    date = datetime.datetime.now()
    if date.day == 1 and date.month == 1:
        return render(req, ("newyear.html"), {"ans":"YES"})
    else :
       return render(req, ("newyear.html"), {"ans":"NO"})

