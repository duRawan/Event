from django.shortcuts import render , redirect ,get_object_or_404
from .models import *
from .forms import EventForm, RegistrationForm, UserLoginForm
from django.template.loader import get_template
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail

def index(request):
    if 'hasEvent' in request.session: 
        request.session['hasEvent']=False
    if 'ErrorRegister' in request.session:
        request.session['ErrorRegister']=""
    if 'message' in request.session:
        request.session['message']=""
    if 'ErrorPassword' in request.session:
        request.session['ErrorPassword']=""
    if not 'logged'  in request.session:
        request.session['logged']=False
    if 'email' in request.session:
        request.session['email']=""
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
    if not 'UID' in request.session:
        context={
        "Event":Event.objects.get(id=id),
        }
    else:
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
        event.description=request.POST.get("description")
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
        U=RegistrationForm(request.POST or None)
        if U.is_valid():
            try:
                us=get_object_or_404(User, email=request.POST['email'])
                request.session['ErrorRegister']=" email already exist"
                if len(request.POST['password'])<8:
                    request.session['ErrorPassword']=" password must be 8 character"
                return redirect("/registerPage")
            except Exception as e:
                U.save()
                email=request.POST['email']
                user=User.objects.get(email=email)
                request.session['logged']=True
                request.session['UID']=user.id
                return redirect("/")
        
        context={
                "User":U ,
            }
    return render(request,"app1/registerPage.html",context)

def loginPage(request):
    if request.session['logged']==True:
        return redirect("/profile")
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
        del request.session['message']
        if 'hasEvent' in request.session: 
            request.session['hasEvent']=False
        if 'ErrorRegister' in request.session:
            request.session['ErrorRegister']=""
        if 'message' in request.session:
            request.session['message']=""
        if 'ErrorPassword' in request.session:
            request.session['ErrorPassword']=""
        if 'logged'  in request.session:
            request.session['logged']=False
        if 'email' in request.session:
            request.session['email']=""

        return redirect("/")

def profile(request):
    user=User.objects.get(id=request.session['UID'])
    context={
        'user':user,
        'allEvent':user.events.values()
    }
    print(context)
    return render(request,'app1/profile.html',context)


def sendEmail(request,event):
    u=User.objects.get(id=request.session['UID'])
    sender_email = "vsecure4@gmail.com"
    receiver_email =u.email #user email
    password = 'Rrdsm@123'
    e=u.events.last()
    print(e)
    message = MIMEMultipart("alternative")
    message["Subject"] = "your Ticket!"
    message["From"] = sender_email
    message["To"] = receiver_email
    result="your ticket"

    d = {'first_name': u.first_name,'last_name':u.last_name,'Event':event}
    htmly = get_template('app1/mail.html')
    print (htmly)
    html_content = htmly.render(d)
    part2 = MIMEText(html_content, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    #message.attach(part1)
    message.attach(part2)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return True
def bookEvent(request,id):
    try:
        this_event = Event.objects.get(id=id)
        user = User.objects.get(id=request.session['UID'])
        e=user.events.values()
        print(this_event.name)
        for i in range(len(e)):
            for k,v in e[i].items():
                if k=='name':
                    x=v
                    if this_event.name==x:
                        print("the event is exist")
                        request.session['hasEvent']=True
                        return redirect(f'/Event/{id}')

        user.events.add(this_event)
        sendEmail(request,this_event.name)
        print("Seeeeennnnnnnddddddddd!!!!!!!!!")
        request.session['hasEvent']=True
        request.session['email']=""
        return redirect(f'/Event/{id}')
    except Exception as e:
        request.session['email']="failed"
        return redirect(f'/Event/{id}')
    

#//////////////////////For testing page

def Registration(request):
    return render(request, "app1/Registration.html")

def Login(request):
    return render(request, "app1/Login.html")

def Contact(request):
    return render(request, "app1/contact.html")

def editProfile(request,id):
    try:
        u=get_object_or_404(User, email=request.POST['email'])
        return redirect(f'/profile')
    except Exception as e:
        user=User.objects.get(id=id)
        user.first_name=request.POST["first_name"]
        user.last_name=request.POST["last_name"]
        user.email=request.POST["email"]
        user.save()
        return redirect(f'/profile')

def editProfProcess(request,id):
    context={
        "user":User.objects.get(id=id)
    }
    return render(request,"app1/editProfile.html",context)
