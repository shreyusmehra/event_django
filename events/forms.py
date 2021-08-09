from django import forms
from django.forms import ModelForm, fields
from .models import Venue, Event


#create a venue form

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address','pin_code', 'phone', 'website', 'email')
        labels ={
            'name' : '',
            'address' : '',
            'pin_code' : '',
            'phone': '',
            'website' : '',
            'email' : '',

        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'pin_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pin Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'website' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')
        labels ={
            'name' : '',
            'event_date' : 'YYYY-MM-DD HH:MM:SS',
            'venue' : 'Venue',
            'manager': 'Manager',
            'attendees' : 'Attendees',
            'description' : '',

        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
            'venue' : forms.Select(attrs={'class':'form-control', 'placeholder':'Venue'}),
            'manager': forms.Select(attrs={'class':'form-control', 'placeholder':'Manager'}),
            'attendees' : forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }