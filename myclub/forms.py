from django import forms
from .models import EventApplication, Offer, Event, OfferApplication, Review, UserRatings
from django.forms.widgets import DateInput, TimeInput



choices = [('Technology','Technology'),
           ('Art','Art'),
           ('Culinary','Culinary'),
           ('Finance','Finance'),
           ('Business','Business')]

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['offerPicture','offerName','offerDescription', 'offerCategory',
                  'offerDate','offerTime','offerDuration','offerCapacity','offerMap']
        widgets = { 
            'offerName':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Offer Name'}),
            'offerDescription':forms.Textarea(attrs={'rows': '5','class': 'form-control','placeholder': 'Offer Description'}), 
            'offerCategory':forms.Select(choices= choices, attrs={'class': 'form-control'}),
            'offerDate': DateInput(attrs={'type': 'date'}),
            'offerTime': TimeInput(format=('%H:%M'),attrs={'type': 'time'}),
            'offerDuration': forms.NumberInput(),
            'offerCapacity': forms.NumberInput(),
            # 'offerLocation':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Offer Location'}),
        }

      
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventPicture','eventName','eventDescription', 'eventCategory','eventDate','eventTime','eventCapacity','eventMap']
        widgets = { 
            'eventName':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Event Name'}),
            'eventDescription':forms.Textarea(attrs={'rows': '5','class': 'form-control','placeholder': 'Event Description'}), 
            'eventCategory':forms.Select(choices= choices, attrs={'class': 'form-control'}),
            'eventDate': DateInput(attrs={'type': 'date'}),
            'eventTime': TimeInput(format=('%H:%M'),attrs={'type': 'time'}),
            #'eventTime': forms.TimeField(widget=SelectDateWidget(minute_step=10, second_step=10)), (https://bradmontgomery.net/blog/selecttimewidget-a-custom-django-widget/)
            'eventCapacity': forms.NumberInput(),
            # 'eventLocation':forms.Textarea(attrs={'rows': '1','class': 'form-control','placeholder': 'Event City'}),
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

class EventApplicationForm(forms.ModelForm):    

    class Meta:
        model = EventApplication
        fields = []

class RatingForm(forms.ModelForm):
    RatingList =(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    feedback = forms.CharField(
        label = 'Feedback',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Please leave your comment here...'
        })
    )
    rating = forms.ChoiceField(
        label = 'Rating',
        choices = RatingList
    )

    class Meta:
        model = UserRatings
        fields = ['rating', 'feedback']
