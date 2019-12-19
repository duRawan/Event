from django.shortcuts import render
from .models import *
from .forms import EventForm

def index(request):
    return render(request, "app1/index.html")

def AdminDash(request):
    form=EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
       "form":form ,
       "allEvents":Event.objects.all()
    }
    return render(request,"app1/AdminDash.html",context)

def showEvent(request,id):
    context={
       "Event":Event.objects.get(id=id)
    }
    print(context)
    return render(request,"app1/ShowEvent.html",context)
