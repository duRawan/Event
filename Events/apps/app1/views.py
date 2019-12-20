from django.shortcuts import render , redirect ,get_object_or_404
from .models import *
from .forms import EventForm, UserForm, UserLoginForm

def index(request):
    context={
       "allEvents":Event.objects.all()
    }
    return render(request, "app1/index.html",context)

def AdminDash(request):
    form=EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
       "form":form ,
       "allEvents":Event.objects.all(),
       "allUsers":User.objects.all()
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

def registerPage(request):
    User=UserForm(request.POST or None)
    if User.is_valid():
        User.save()
    else:
        print("Errrrrrrrroooooorrrrrr")
    
    context={
            "User":User ,
        }
    return render(request,"app1/registerPage.html",context)

def loginPage(request):
    user=UserLoginForm(request.POST or None)
    
    context={
            "User":user ,
        }
    return render(request,"app1/loginPage.html",context)

def register(request):
    pass
#Log in is Need To be refactored !! #decorator for ensuring that a user is loged in  !! 
def login(request):
    # u=User.objects.filter(email=request.POST['email'],password=request.POST['password'])
    us=get_object_or_404(User, email=request.POST['email'])#use object or 404
    ps=get_object_or_404(User, password=request.POST['password'])
    if us:
        if ps:
            print("Exist")
            return redirect("/")
    else:
        return redirect("/loginPage")

