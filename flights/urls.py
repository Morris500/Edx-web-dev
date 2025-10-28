from django.urls import path
from . import views


urlpatterns = [
path("", views.index, name="index"),
path("<int:flight_id>/", views.flight_detail, name="flight_detail"),
path("<int:flight_id>/book", views.book, name="book"),

]