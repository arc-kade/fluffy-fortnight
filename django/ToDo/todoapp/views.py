from django.http import HttpResponse #custom import
from django.shortcuts import render #to return HTML files
from todoapp.models import ToDos


# Create your views here.
def Home(request): #user defined function
    is_authenticated = True
    # myTasks=["Complete LMS tasks", "Attend Soft skill session", "Learn React", "Complete Django Project"]
    myTasks = ToDos.objects.all() #SELECT* FROM in SQL
    print(myTasks)

    context={"task":myTasks,"status":is_authenticated}
    return render(request,"index.html",{"tasks": myTasks}) #calls /templates/index.html

def TestResponse(request):
    return HttpResponse("Hello world")

def About(request):
    return render(request,"about.html")

def Contact(request):
    return render(request,"contact.html")
