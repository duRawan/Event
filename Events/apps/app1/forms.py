
from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'numberOfTickets']
        widget={
            
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
            })
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','password']
        widget={
            'first_name': forms.TextInput(attrs={
                'placeholder':"Enter your first name",
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder':"Enter your last name",
            }),
            'email': forms.TextInput(attrs={
                'placeholder':"Enter your email",
            }),
            'password': forms.TextInput(attrs={
                'placeholder':"Enter your password",
                'name':'password'
            })
        }
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password']
        widget={
            'email': forms.TextInput(attrs={
                'placeholder':"Enter your email",
                'class':'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder':"Enter your password",
                'class':'form-control',
            })
        }