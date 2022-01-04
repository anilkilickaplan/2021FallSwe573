from django.core.checks import messages
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls.base import reverse
from django.views import View
from .models import EventApplication, Offer, OfferApplication, UserProfile, Event, Review, UserRatings
from .forms import EventApplicationForm, OfferApplicationForm, OfferForm, EventForm, RatingForm, ReviewForm
from django.views.generic.edit import UpdateView, DeleteView
import datetime
from django.contrib import  messages
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from geopy.geocoders import Nominatim
from django.db.models import Avg





# OFFER RELATED 
class OfferListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        searchOffer= request.GET.get('q')
        offer_list_category = request.GET.get('offer_list_category')
        offers = Offer.objects.all().order_by('-offerCreatedDate')
        form = OfferForm()

        try:
            searchOffer = self.request.GET['q']
            offer_list_category = self.request.GET['offer_list_category']
        except:
            searchOffer = ''
            offer_list_category='General'

        if searchOffer != '':
            offers  = offers.filter(Q (offerName__icontains = searchOffer) | 
                                    Q (offerDescription__icontains = searchOffer)|
                                    Q (offerCategory__icontains = searchOffer) ) 
            if offers =='':
                messages.warning(request,"No match with the keyword")

        if offer_list_category != '':
            offers  = offers.filter(offerCategory = offer_list_category) 
            if offers =='':
                messages.warning(request,"No match with the category")
        
        if searchOffer =='' and offer_list_category=='General':
            offers = Offer.objects.all().order_by('-offerCreatedDate') 

        paginator = Paginator(offers, 5) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'offer_list': offers,
            'form': form,
            'page_obj': page_obj
        }
        
        return render(request, 'myclub/offer_list.html', context)


  
class OfferCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = OfferForm()
        
        context = {
            'form': form,
        }

        return render(request, 'myclub/create_offer.html', context)

    def post(self, request, *args, **kwargs):
        form = OfferForm(request.POST, request.FILES)
        owner_profile = UserProfile.objects.get(pk=request.user)

        if form.is_valid():
            totalcredit = owner_profile.userReservehour + owner_profile.userCredits
            new_offer = form.save(commit=False)
            if totalcredit + new_offer.offerDuration <= 15:
                new_offer.offerOwner = request.user
                owner_profile.userReservehour = owner_profile.userReservehour + new_offer.offerDuration
                owner_profile.save()
                new_offer.save()
                
                messages.success(request,'Offer is created')
            else:
                messages.warning(request, 'Your credits and pending offer durations cannot exceed 15.')
        else:
            messages.warning(request, 'Form is not valid, please check the values')

       
        myoffers = Offer.objects.filter(offerOwner = request.user)
        return render(request, 'myclub/my_offers_list.html', {'myoffers':myoffers})


        #return redirect('offer-detail')

class OfferDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(pk=pk)
        #form = OfferForm()
        # form = ReviewForm()
        
        current_time = datetime.datetime.now().time()
        current_date = datetime.datetime.now()
        applications = OfferApplication.objects.filter(appliedOffer=pk).order_by('-applicationDate')
        applications_this = applications.filter(applicant=request.user)
        number_of_accepted = len(applications.filter(isApproved=True))
        accepted_applications = applications.filter(isApproved=True)
        application_number = len(applications)
        is_active = True
        comments = UserRatings.objects.filter(offer=offer)


        if offer.offerDate <= current_date.date():
            if offer.offerTime < current_time:
                is_active = False
        if len(applications) == 0:
            is_applied = False
            is_accepted = False
        for application in applications:
            if application.applicant == request.user:
                is_applied = True
                is_accepted = application.isApproved
                break
            else:
                is_applied = False
                is_accepted = False
       
        geolocator = Nominatim(user_agent = "app.name")
        offerAddress= geolocator.reverse(offer.offerMap)
                

        context = {
            'offer': offer,
            'applications': applications,
            'number_of_accepted': number_of_accepted,
            'is_applied': is_applied,
            'applications_this': applications_this,
            'is_accepted': is_accepted,
            'is_active': is_active,
            'application_number': application_number,
            'accepted_applications': accepted_applications,
            'current_time':current_time,
            'current_date': current_date,
            'offerAddress': offerAddress.address,
            'comments': comments

        }

        return render(request, 'myclub/offer_detail.html', context)


    def post(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(pk=pk)
        form = OfferApplicationForm(request.POST)
        applications = OfferApplication.objects.filter(appliedOffer=pk).order_by('-applicationDate')
        applications_this = applications.filter(applicant=request.user)
        number_of_accepted = len(applications.filter(isApproved=True))
        applicant_user_profile = UserProfile.objects.get(pk=request.user)
   
        if len(applications) == 0:
            is_applied = False
        for application in applications:
            if application.applicant == request.user:
                is_applied = True
                break
            else:
                is_applied = False

        if form.is_valid():

            if is_applied == False:
                totalcredit = applicant_user_profile.userReservehour + applicant_user_profile.userCredits
                if totalcredit >= offer.offerDuration:
                    new_application = form.save(commit=False)
                    new_application.applicant = request.user
                    new_application.appliedOffer = offer
                    new_application.isApproved = False
                    new_application.save()
                    applicant_user_profile.userReservehour = applicant_user_profile.userReservehour - offer.offerDuration
                    applicant_user_profile.save()
                    messages.success(request, 'Your applied for the offer')
                else:
                    messages.warning(request, 'Please check your available credits')

        context = {
            'offer': offer,
            'form': form,
            'applications': applications,
            'number_of_accepted': number_of_accepted,
            'is_applied': is_applied,
            'applications_this': applications_this,
        }

        return redirect('offer-detail', pk=offer.pk) 

class OfferEditView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        offer = Offer.objects.get(pk=pk)

        if offer.offerOwner == request.user:
            if offer.offerDate > timezone.now().date():

                form = OfferForm(instance = offer)
                context = {
                    'form': form,
                }

                return render(request, 'myclub/offer_edit.html', context)
            else:
                return redirect('offer-detail', pk=offer.pk)
        else:
            return redirect('offer-detail', pk=offer.pk)

    def post(self, request, *args, **kwargs):
        form = OfferForm(request.POST, request.FILES)
        pk=self.kwargs['pk']
        offer = Offer.objects.get(pk=pk)
       
        if form.is_valid():
            edit_offer = form.save(commit=False)
            if request.FILES:
                offer.offerPicture = edit_offer.offerPicture
            offer.offerName = edit_offer.offerName
            offer.offerDescription= edit_offer.offerDescription
            offer.offerCategory=edit_offer.offerCategory
            offer.offerLocation=edit_offer.offerLocation
            offer.offerMap=edit_offer.offerMap
            offer.offerDate=edit_offer.offerDate
            offer.offerTime=edit_offer.offerTime
            offer.save()
        else:
            messages.WARNING(request,("There is a problem with editing the offer"))


        return redirect('offer-detail', pk)
    
class OfferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offer
    template_name = 'myclub/offer_delete.html'
    success_url = reverse_lazy('offer-list')

    def test_func(self):
        offer = self.get_object()
        return self.request.user == offer.offerOwner


# EVENT RELATED
class EventListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        searchEvent= request.GET.get('q')
        event_list_category = request.GET.get('offer_list_category')
        events = Event.objects.all().order_by('-eventCreatedDate')
        form = EventForm()
        current_time = timezone.now().date()
        
        try:
            searchEvent = self.request.GET['q']
            event_list_category = self.request.GET['event_list_category']
        except:
            searchEvent = ''
            event_list_category='General'

        if searchEvent != '':
            events  = events.filter(Q (eventName__icontains = searchEvent) | 
                                    Q (eventDescription__icontains = searchEvent)|
                                    Q (eventCategory__icontains = searchEvent) ) 
            if events =='':
                messages.warning(request,"No match with the keyword")

        if event_list_category != '':
            events  = events.filter(eventCategory= event_list_category)
            if events =='':
                messages.warning(request,"No match with the category")
        
        if searchEvent =='' and event_list_category=='General':
            events = Event.objects.all().order_by('-eventCreatedDate') 

        paginator = Paginator(events, 5) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'event_list': events,
            'form': form,
            'page_obj': page_obj,
            'current_time': current_time
        }

        return render(request, 'myclub/event_list.html', context)

class EventCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = EventForm()
        
        context = {
            'form': form,
        }

        return render(request, 'myclub/create_event.html', context)

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.eventOwner = request.user
            new_event.save()
        else:
            messages.warning(request, 'Form is not valid')
            
        myevents = Event.objects.filter(eventOwner = request.user).order_by('-eventCreatedDate')
        return render(request, 'myclub/my_events_list.html', {'myevents':myevents})

        # return redirect('myevents-list')

class EventDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        event = Event.objects.get(pk=pk)
        #form = EventForm()
        # form = ReviewForm()
        current_time = datetime.datetime.now().time()
        current_date = datetime.datetime.now()
        applications = EventApplication.objects.filter(appliedEvent=pk).order_by('-applicationDate')
        applications_this = applications.filter(applicant=request.user)
        number_of_accepted = len(applications.filter(isApproved=True))
        accepted_applications = applications.filter(isApproved=True)
        application_number = len(applications)
        is_active = True

        if event.eventDate <= current_date.date():
            if event.eventTime < current_time:
                is_active = False
        if len(applications) == 0:
            is_applied = False
            is_accepted = False
        for application in applications:
            if application.applicant == request.user:
                is_applied = True
                is_accepted = application.isApproved
                break
            else:
                is_applied = False
                is_accepted = False

        context = {
            'event': event,
            'applications': applications,
            'number_of_accepted': number_of_accepted,
            'is_applied': is_applied,
            'applications_this': applications_this,
            'is_accepted': is_accepted,
            'is_active': is_active,
            'application_number': application_number,
            'accepted_applications': accepted_applications
        }

        return render(request, 'myclub/event_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
       
        event = Event.objects.get(pk=pk)
        form = EventApplicationForm(request.POST)
        applications = EventApplication.objects.filter(appliedEvent=pk).order_by('-applicationDate')
        applications_this = applications.filter(applicant=request.user)
        number_of_accepted = len(applications.filter(isApproved=True))
        applicant_user_profile = UserProfile.objects.get(pk=request.user)
   
        if len(applications) == 0:
            is_applied = False
        for application in applications:
            if application.applicant == request.user:
                is_applied = True
                break
            else:
                is_applied = False

        if form.is_valid():

            if is_applied == False:
            
                new_application = form.save(commit=False)
                new_application.applicant = request.user
                new_application.appliedEvent = event
                if number_of_accepted < event.eventCapacity:
                    new_application.isApproved = True
                else:
                    new_application.isApproved = False
                new_application.save()
                applicant_user_profile.save()
                messages.success(request, 'Your applied for the event')
      

        context = {
            'event': event,
            'form': form,
            'applications': applications,
            'number_of_accepted': number_of_accepted,
            'is_applied': is_applied,
            'applications_this': applications_this,
        }

        return redirect('event-detail', pk=event.pk) 

class EventEditView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        event = Event.objects.get(pk=pk)
        if event.eventOwner == request.user:
            if event.eventDate > timezone.now().date():
           
                form = EventForm(instance = event)
                context = {
                    'form': form,
                 }
                return render(request, 'myclub/event_edit.html', context)
            else:
                return redirect('event-detail', pk=event.pk)
        else:
            return redirect('event-detail', pk=event.pk)

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        pk=self.kwargs['pk']
        event = Event.objects.get(pk=pk)

        if form.is_valid():
            edit_event = form.save(commit=False)
            if request.FILES:
                event.eventPicture = edit_event.eventPicture
            event.eventName = edit_event.eventName
            event.eventDescription= edit_event.eventDescription
            event.eventCategory=edit_event.eventCategory
            event.eventLocation=edit_event.eventLocation
            event.eventMap=edit_event.eventMap
            event.eventDate=edit_event.eventDate
            event.eventTime=edit_event.eventTime
            event.save()


        return redirect('event-detail', pk)

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'myclub/event_delete.html'
    success_url = reverse_lazy('event-list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.eventOwner

# USER PROFILE RELATED
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        userfollowers = user.userfollowers.all()
        ratings_average = UserRatings.objects.filter(rated=profile.user).aggregate(Avg('rating'))
        comments = UserRatings.objects.filter(rated=profile.user)

        if len(userfollowers) == 0:
            is_following = False
        for follower in userfollowers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False
        
        
        number_of_followers = len(userfollowers)
        context = {
            'user': user,
            'profile': profile,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'ratings_average': ratings_average,
            'comments': comments

        }
        return render(request, 'myclub/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['userPicture', 'userName', 'userBio', 'userBirthDate', 'userLocation']
    template_name = 'myclub/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


def allEvents (request): 
    event_list = Event.objects.all()
    return render (request, 'myclub/event_list.html', 
    {'event_list': event_list})

def allOffers (request): 
    offer_list = Event.objects.all()
    return render (request, 'myclub/offer_list.html', 
    {'offer_list': offer_list})

def searchEvents(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains = searched)

        return render (request, 
        'myclub/search_events.html', 
            {'searched': searched, 'events':events})
    else:
        return render(request, 
        'myclub/search_events.html',
        {})



def home(request, year=datetime.datetime.now().year, month=datetime.datetime.now().strftime('%B')):
    return render (request, 'myclub/home.html', 
    {})

class myEventsView(View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            myevents = Event.objects.filter(eventOwner = request.user.id)
            return render(request, 
            'myclub/my_events_list.html', 
            {'myevents':myevents})
        else:
            messages.WARNING(request,("There is a problem with authentication. my_events (views) could not fetch user authentication"))

class myOffersView(View):
    def get(self, request, pk, *args, **kwargs):
            
        if request.user.is_authenticated:
            # myoffers = Offer.objects.filter(offerOwner=me)
            myoffers = Offer.objects.filter(offerOwner = request.user.id).order_by('-offerCreatedDate')
            return render(request, 
            'myclub/my_offers_list.html', 
            {'myoffers':myoffers})

        else:
            messages.WARNING(request,("There is a problem with authentication. my_offers (views) could not fetch user authentication"))




class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        follow_pk = self.kwargs['followpk']
        profile = UserProfile.objects.get(pk=pk)
        profile.userFollowers.add(request.user)
        return redirect('profile', pk=follow_pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        follow_pk = self.kwargs['followpk']
        profile = UserProfile.objects.get(pk=pk)
        profile.userFollowers.remove(request.user)
        return redirect('profile', pk=follow_pk)

class RemoveMyFollower(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        userFollower_pk = self.kwargs['userFollower_pk']
        userFollower = UserProfile.objects.get(pk=userFollower_pk).user
        profile = UserProfile.objects.get(pk=request.user.pk)
        profile.userFollowers.remove(userFollower)
        
        return redirect('userFollowers', pk=request.user.pk)

class FollowersListView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        userFollowers = profile.userFollowers.all()

        context = {
            'userFollowers': userFollowers,
            'profile': profile,
        }

        return render(request, 'myclub/userfollowers_list.html', context)


class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = OfferApplication
    template_name = 'myclub/application_delete.html'

    def get_success_url(self):
        pk = self.kwargs['offer_pk']
        return reverse_lazy('offer-detail', kwargs={'pk': pk})
    
    def test_func(self):
        application = self.get_object()
        return self.request.user == application.applicant

class ApplicationEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OfferApplication
    fields = ['isApproved']
    template_name = 'myclub/application_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['offer_pk']
        return reverse_lazy('offer-detail', kwargs={'pk': pk})
    
    def test_func(self):
        application = self.get_object()
        return self.request.user == application.appliedOffer.offerOwner


class EventApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EventApplication
    template_name = 'myclub/event-application_delete.html'

    def get_success_url(self):
        event_pk = self.kwargs['event_pk']
        event = Event.objects.get(pk=event_pk)
        application = self.get_object()
        applicant_user_profile = UserProfile.objects.get(pk=application.applicant.pk)
        applicationsNext = EventApplication.objects.filter(appliedEvent=event).filter(isApproved=False).order_by('-applicationDate')
        count = 0
        for applicationNext in applicationsNext:
            if count == 0:
                applicationNext.isApproved = True
                applicationNext.save()
                count = 1
        return reverse_lazy('event-detail', kwargs={'pk': event_pk})
    
    def test_func(self):
        application = self.get_object()
        isOK = False
        if self.request.user == application.applicant:
            isOK = True
        if self.request.user == application.appliedEvent.eventOwner:
            isOK = True
        return isOK




class ConfirmOfferTaken(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(pk=pk)
        offer.is_taken = True
        offer.save()
        CreditExchange(offer)
        return redirect('offer-detail', pk=pk)

class ConfirmOfferGiven(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(pk=pk)
        offer.is_given = True
        offer.save()
        CreditExchange(offer)
        return redirect('offer-detail', pk=pk)

def CreditExchange(offer):
    applications = OfferApplication.objects.filter(appliedOffer=offer.pk).filter(isApproved=True)
    if offer.is_taken == True:
        if offer.is_given == True:
            offer_giver = UserProfile.objects.get(pk=offer.offerOwner.pk)
            offer_giver.userCredits = offer_giver.userCredits + offer.offerDuration
            offer_giver.userReservehour = offer_giver.userReservehour - offer.offerDuration
            offer_giver.save()
            for application in applications:
                offer_taker = UserProfile.objects.get(pk=application.applicant.pk)
                offer_taker.userCredits = offer_taker.userCredits - offer.offerDuration
                offer_taker.userReservehour = offer_taker.userReservehour + offer.offerDuration
                offer_taker.save()
    return redirect('offer-detail', pk=offer.pk)



class RateUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = RatingForm()
        offerpk = self.kwargs['offerpk']
        offer = Offer.objects.get(pk=offerpk)
        ratedpk = self.kwargs['ratedpk']
        rated = UserProfile.objects.get(user=ratedpk)
        ratingRecord = UserRatings.objects.filter(offer=offer).filter(rated=rated.user).filter(rater=request.user)
        isRated = len(ratingRecord)

        context = {
            'form': form,
            'ratingRecord': ratingRecord,
            'isRated': isRated,
            'rated': rated,
            'offer': offer,
        }

        return render(request, 'myclub/rating.html', context)

    def post(self, request, *args, **kwargs):
        form = RatingForm(request.POST)
        offerpk = self.kwargs['offerpk']
        offer = Offer.objects.get(pk=offerpk)
        ratedpk = self.kwargs['ratedpk']
        rated = UserProfile.objects.get(user=ratedpk)

        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.rater = request.user
            new_rating.offer = offer
            new_rating.rated = rated.user
            new_rating.save()
            messages.success(request, 'Your rate is submitted')

        return redirect('offer-detail', pk=offerpk)

class RateUserEdit(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        rating = UserRatings.objects.get(pk=pk)
        form = RatingForm(instance = rating)     
        context = {
            'form': form,
            'rating': rating,
        }
        return render(request, 'myclub/rating-edit.html', context)

    def post(self, request, *args, pk, **kwargs):
        form = RatingForm(request.POST)
        rating = UserRatings.objects.get(pk=pk)

        if form.is_valid():
            edit_rating = form.save(commit=False)
            rating.rating = edit_rating.rating
            rating.feedback = edit_rating.feedback
            rating.save()        
            messages.success(request, 'Rating update is submitted')

        context = {
            'form': form,
        }

        return render(request, 'myclub/rating-edit.html', context)

class RateUserDelete(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        rating = UserRatings.objects.get(pk=pk)

        form = RatingForm(instance = rating)
        context = {
            'form': form,
        }

        return render(request, 'myclub/rating-delete.html', context)

    def post(self, request, *args, pk, **kwargs):
        rating = UserRatings.objects.get(pk=pk)
        offer = rating.offer
        rating.delete()
        return redirect('offer-detail', pk=offer.pk)

