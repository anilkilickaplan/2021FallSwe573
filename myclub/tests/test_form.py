 
from myclub.forms import OfferForm, EventForm
import datetime
from django.test import TestCase

class EventFormTest(TestCase):
    def test_event_form_name_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['eventName'].label == 'Name')

    def test_event_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = EventForm(data={'eventDate': date})
        
        self.assertFalse(form.is_valid())

class OfferFormTest(TestCase):
    def test_offer_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = OfferForm(data={'offerDate': date})
        self.assertFalse(form.is_valid())