from django.shortcuts import render , redirect
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

def editProcess(request,id):
    context={
       "Event":Event.objects.get(id=id)
    }
    return render(request,"app1/edit.html",context)


def editEvent(request,id):
    event=Event.objects.get(id=id)
    event.name=request.POST["name"]
    event.description=request.POST["desc"]
    event.numberOfTickets=request.POST["number"]
    event.save()
    return redirect(f'/Event/{event.id}')
    



def deleteEvent(request,id):
    event=Event.objects.get(id=id)
    event.delete()
    return redirect("/admindashboard")