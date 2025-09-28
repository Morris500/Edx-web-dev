from django.urls import path
from index import views


urlpatterns = [
path ("", views.index, name="index"),
path ("hello", views.hello, name="hello"),
path ("<str:name>", views.greet, name="greet")
]
