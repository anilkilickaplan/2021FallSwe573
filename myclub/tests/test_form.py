 
from myclub.forms import OfferForm, EventForm
import datetime
from django.test import TestCase


# fields = ['offerPicture','offerName','offerDescription', 'offerCategory',
#                   'offerDate','offerTime','offerDuration','offerCapacity','offerLocation','offerMap']
class OfferFormTest(TestCase):
    def test_offer_form_false(self):
        
        form_data =  {
        'offerPicture':'uploads/offer_pictures/',
        'offerName':'testOfferName',
        'offerDescription':'TestofferDescription', 
        'offerCategory':'Technology',
        'offerDate':'2022-01-01',
        'offerTime':'1:03',
        'offerDuration':'2',
        'offerCapacity':'12',
        'offerLocation':'Manisa',
        'offerMap':'41.031964, 29.008841'}
        form = OfferForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_offer_form_valid_true(self):
        
        form_data =  {
        'offerPicture':'uploads/offer_pictures/',
        'offerName':'testOfferName',
        'offerDescription':'TestofferDescription', 
        'offerCategory':'Technology',
        'offerDate':'2022-11-11',
        'offerTime':'1:03',
        'offerDuration':'2',
        'offerCapacity':'12',
        'offerLocation':'Manisa',
        'offerMap':'41.031964, 29.008841'}
        form = OfferForm(data = form_data)
        self.assertTrue(form.is_valid())

#fields = ['eventPicture','eventName','eventDescription', 'eventCategory','eventDate','eventTime','eventCapacity','eventMap']

class EventFormTest(TestCase):
    def test_event_form_false(self):
        
        form_data =  {
        'eventPicture':'uploads/event_pictures/',
        'eventName':'testEventName',
        'eventDescription':'TesteventDescription', 
        'eventCategory':'Technology',
        'eventDate':'2022-01-01',
        'eventTime':'1:03',
        'eventDuration':'2',
        'eventCapacity':'12',
        'eventLocation':'Manisa',
        'eventMap':'41.031964, 29.008841'}
        form = EventForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_event_form_valid_true(self):
        
        form_data =  {
        'eventPicture':'uploads/event_pictures/',
        'eventName':'testEventName',
        'eventDescription':'TesteventDescription', 
        'eventCategory':'Technology',
        'eventDate':'2022-11-11',
        'eventTime':'1:03',
        'eventDuration':'2',
        'eventCapacity':'12',
        'eventLocation':'Manisa',
        'eventMap':'41.031964, 29.008841'}
        form = EventForm(data = form_data)
        self.assertTrue(form.is_valid())
