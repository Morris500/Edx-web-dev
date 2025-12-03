from django.shortcuts import render
from django.middleware.csrf import get_token

# Create your views here.

data = [" lorem Lorem ipsum dolor sit amet consectetur adipisicing elit iiiiii. ", 
"Eius eum aperiam molestias doloremque non obcaecati eveniet est dolores!eeee",
" Animi exercitationem unde ut nemo placeat assumenda nam tempora consequatur corrupti odio. "]
def interface(req):
    csrf_token = get_token(req)
    if req.method == 'POST':
        print(req.POST.get)
    return render (req, "interface.html", {"datas": data})

