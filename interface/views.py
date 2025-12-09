from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse
import json

# Create your views here.

data = [
    " lorem Lorem ipsum dolor sit amet consectetur adipisicing elit iiiiii. ",
    "Eius eum aperiam molestias doloremque non obcaecati eveniet est dolores!eeee",
    " Animi exercitationem unde ut nemo placeat assumenda nam tempora consequatur corrupti odio. "
]

def interface(req):
    csrf_token = get_token(req)
    if req.method == 'POST':
        body = json.loads(req.body.decode('utf-8'))  # parse JSON
        num = int(body.get("value"))
        result = data[num]
        print(result)
        return JsonResponse({"status": "ok", "received": result})
        
    
    return render(req, "interface.html" )