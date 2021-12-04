from django import forms
from django.forms import ModelForm
from .models import Offer, Event, OfferApplication, Review
from django.forms.widgets import DateInput, TimeInput



class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['offerName','offerDescription', 'offerDate','offerTime','offerDuration','offerCapacity','offerLocation']
        widgets = { 
            'offerName':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Offer Name'}),
            'offerDescription':forms.Textarea(attrs={'rows': '5','class': 'form-control','placeholder': 'Offer Description'}), 
            'offerDate': DateInput(attrs={'type': 'date'}),
            'offerTime': TimeInput(format=('%H:%M'),attrs={'type': 'time'}),
            'offerDuration': forms.NumberInput(),
            'offerLocation':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Offer Location'}),
        }
        
        

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventName','eventDescription', 'eventDate','eventTime','eventCapacity','eventLocation']
        widgets = { 
            'eventName':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Event Name'}),
            'eventDescription':forms.Textarea(attrs={'rows': '5','class': 'form-control','placeholder': 'Event Description'}), 
            'eventDate': DateInput(attrs={'type': 'date'}),
            'eventTime': TimeInput(format=('%H:%M'),attrs={'type': 'time'}),
            'eventCapacity': forms.NumberInput(),
            'eventLocation':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Event City'}),
        }
        



class ReviewForm(forms.ModelForm):
    review = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Give Review'}
        ))

    class Meta:
        model = Review
        fields = ['review']

class OfferApplicationForm(forms.ModelForm):    

    class Meta:
        model = OfferApplication
        fields = []