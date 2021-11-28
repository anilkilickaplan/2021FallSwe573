from django import forms
from .models import Offer, Event, Feedback


class OfferForm(forms.ModelForm):
    
    offerName = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Offer Name'
        })
    )
    
       
    
    offerDescription = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Create an offer'
        })
    )

    offerDate = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M:%S'),
    )
    
    offerCapacity = forms.IntegerField(
    )

    class Meta:
        model = Offer
        fields = ['offerName','offerDescription', 'offerDate' ,'offerCapacity']


class EventForm(forms.ModelForm):
    eventName = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Event name'
        })
    )

    eventDescription = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Event description'
        })
    )

    eventDate = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M'),
    )

    eventCapacity = forms.IntegerField(
    )

    class Meta:
        model = Event
        fields = ['eventName', 'eventDescription', 'eventDate', 'eventLocation', 'eventCapacity']


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Give Feedback'}
        ))

    class Meta:
        model = Feedback
        fields = ['feedback']
