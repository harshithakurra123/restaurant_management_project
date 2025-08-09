import requests
from django.shortcuts import render

def menu_view(request):
    response=requests.get('http:/localhost:8000/api/menu/')
    menu_items=response.json()if response.status_code==200 else[]

    return render(request,'home/menu.html',{'menu_items':menu_items})

# Create your views here.
      