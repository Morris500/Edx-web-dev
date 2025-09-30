from django.urls import path
from hello import views


urlpatterns = [
path ("", views.hello, name="index"),
# path ("hello", views.hello, name="hello"),
path ("<str:name>", views.greet, name="greet")
]
