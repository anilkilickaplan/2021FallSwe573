
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from myclub.models import Offer
from myclub.views import OfferCreateView
import datetime

class OfferModelTest(TestCase):              
    @classmethod

    def setUp(self):
        self.testuser = User.objects.create(username='usertest1')

    def testOffer(self):
        offer = Offer(
            offerOwner=self.testuser, 
            offerCreatedDate=timezone.now(), 
            offerName="OfferTest",
            offerDescription="OfferTestDescription", 
            offerPicture='uploads/offer_pictures/default.png',
            offerLocation='34.0215563,21.111111',
            offerDate=datetime.datetime.now(),
            offerTime = datetime.datetime.now().time(),
            offerCapacity=1,
            offerDuration=1,
            is_given=False,
            is_taken=False
            )
        self.assertEqual(offer.offerOwner, self.testuser)
        self.assertEqual(offer.offerName, "OfferTest")