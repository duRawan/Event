from django.shortcuts import render , redirect ,get_object_or_404
from .models import *
from .forms import EventForm, UserForm, UserLoginForm

def index(request):
    if not 'logged'  in request.session:
        request.session['logged']=False
    context={
       "allEvents":Event.objects.all(),
       "r":Event.objects.count()
    }
    print("------------------------" ,context)
    
    return render(request, "app1/index1.html",context)

def AdminDash(request):
    if 'logged'  in request.session:
        if request.session['UID']==1:
            form=EventForm(request.POST or None)
            if form.is_valid():
                form.save()
            context={
                "form":form ,
                "allEvents":Event.objects.all(),
                "allUsers":User.objects.all()
            }
            return render(request,"app1/AdminDash.html",context)
        else:
            return redirect('/')
    return render(request,"app1/AdminDash.html",context)

def showEvent(request,id):
    context={
       "Event":Event.objects.get(id=id),
       "user":request.session['UID']
    }
    print(context)
    return render(request,"app1/ShowEvent.html",context)

def editProcess(request,id):
    if request.session['UID']==1:
        context={
        "Event":Event.objects.get(id=id)
        }
        return render(request,"app1/edit.html",context)
    else:
        return redirect('/')


def editEvent(request,id):
    if request.session['UID']==1:
        event=Event.objects.get(id=id)
        event.name=request.POST["name"]
        event.description=request.POST["desc"]
        event.numberOfTickets=request.POST["number"]
        event.save()
        return redirect(f'/Event/{event.id}')
    else:
        return redirect('/')

def deleteEvent(request,id):
    if request.session['UID']==1:
        event=Event.objects.get(id=id)
        event.delete()
        return redirect("/admindashboard")
    else: 
        return redirect('/')

def registerPage(request):
    if request.session['logged']==True:
        # return redirect("/")
        return redirect("/profile")
    else:
        User=UserForm(request.POST or None)
        if User.is_valid():
            User.save()
            request.session['logged']=True
            request.session['UID']=User.id
            return redirect("/")
        
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


#Log in is Need To be refactored Email must be unique!! #decorator for ensuring that a user is loged in  !! 
def login(request):
    if request.session['logged']==True:
        return redirect("/profile")
    # u=User.objects.filter(email=request.POST['email'],password=request.POST['password'])
    else:
        if request.method == "POST":
            password=request.POST['password']
            email=request.POST['email']
            try:
                user=get_object_or_404(User, email=request.POST['email'])
            except Exception as e:
                request.session['message']="wrong email or password, please try again"
                return redirect("/loginPage")
            if password==user.password:
                request.session['logged']=True
                request.session['UID']=user.id
                request.session['message']=""
                return redirect("/")
            else:
                request.session['message']="wrong email or password, please try again"
                return redirect("/loginPage")
        return render(request, "app1/loginPage.html")

def logout(request):
    if not 'logged'  in request.session:
        request.session['logged']=False
        return redirect("/loginPage")
    elif request.session['logged']==False:
        return redirect("/loginPage")
        
    else:
        del request.session['UID']
        request.session['logged']=False
        return redirect("/")

def profile(request):
    user=User.objects.get(id=request.session['UID'])
    context={
        'user':user,
        'allEvent':user.events.values()
    }
    print(context)
    return render(request,'app1/profile.html',context)

def bookEvent(request,id):
    this_event = Event.objects.get(id=id)
    user = User.objects.get(id=request.session['UID'])
    user.events.add(this_event)
    return redirect(f'/Event/{id}')

#//////////////////////For testing page

def Registration(request):
    return render(request, "app1/Registration.html")

def Login(request):
    return render(request, "app1/Login.html")

def Contact(request):
    return render(request, "app1/contact.html")

