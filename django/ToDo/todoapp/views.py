from django.http import HttpResponse #custom import
from django.shortcuts import render #to return HTML files

# Create your views here.
def Home(request): #user defined function
    return render(request,"index.html") #calls /templates/index.html

def TestResponse(request):
    return HttpResponse("Hello world")

def About(request):
    return render(request,"about.html")

def Contact(request):
    return render(request,"contact.html")
