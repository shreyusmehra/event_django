from django import forms
from django.forms import ModelForm, fields
from .models import Venue


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