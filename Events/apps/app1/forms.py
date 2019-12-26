
from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'numberOfTickets','location','photo']
        widgets={
            
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter Event name",
            }),
            
            'description': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter Event description",
            }),
            
            'numberOfTickets': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter number of tickets",
                'type':'number'
            }),
            'location': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter Event location",
            }),
            'photo':forms.FileInput(attrs={
                'class':'browse btn input-group-append'
            })
        }

class RegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','password']
        widgets={
            'first_name': forms.TextInput(attrs={
                'placeholder':"Enter your first name",
                'class':'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder':"Enter your last name",
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'placeholder':"Enter your email",
                'class':'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder':"Enter your password",
                'name':'password',
                'class':'form-control'
            })
        }
class UserLoginForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password']
        widgets={
            'email': forms.TextInput(attrs={
                'placeholder':"Enter your email",
                'class':'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder':"Enter your password",
                'class':'form-control',
            })
        }