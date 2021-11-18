from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def map(request):
    data={"data":"test"}
    return render(request, "map.html", context=data)