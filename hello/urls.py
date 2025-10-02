from django.urls import path
from hello import views


urlpatterns = [
path ("", views.hello, name="index"),
# path ("hello", views.hello, name="hello"),
path ("todolist/", views.todolist, name="todolist"),
path ("add/", views.add, name="add" )
]
