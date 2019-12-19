
from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'numberOfTickets']
        widget={
            'name': forms.TextInput(attrs={
                'placeholder':"Enter Event name",
            }),
            'description': forms.TextInput(attrs={
                'placeholder':"Enter Event description",
            }),
            'numberOfTickets': forms.TextInput(attrs={
                'placeholder':"Enter number of tickets",
            })
        }