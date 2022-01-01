from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    # HOME
    path('home', views.home, name='home'),
    
    # OFFER RELATED
    path('offer', views.OfferListView.as_view(), name='offer-list'),
    path('offer/create', views.OfferCreateView.as_view(), name='offer-create'),
    path('offer/<int:pk>', views.OfferDetailView.as_view(), name='offer-detail'),
    path('offer/edit/<int:pk>', views.OfferEditView.as_view(), name='offer-edit'),
    path('offer/delete/<int:pk>', views.OfferDeleteView.as_view(), name='offer-delete'),
    

    # EVENT RELATED
    path('event', views.EventListView.as_view(), name='event-list'),
    path('event/create', views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('event/edit/<int:pk>', views.EventEditView.as_view(), name='event-edit'),
    path('event/delete/<int:pk>', views.EventDeleteView.as_view(), name='event-delete'),
    
    # PROFILE RELATED
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('myoffers/<int:pk>', views.myOffersView.as_view(), name='myoffers-list'),
    path('myevents/<int:pk>', views.myEventsView.as_view(), name='myevents-list'),

    # Followers
    path('profile/<int:pk>/userfollowers/', views.FollowersListView.as_view(), name='followers'),
    path('profile/<int:pk>/userfollowers/add/<int:followpk>', views.AddFollower.as_view(), name='add-userfollower'),
    path('profile/<int:pk>/userfollowers/remove/<int:followpk>', views.RemoveFollower.as_view(), name='remove-userfollower'),
    path('userfollowers/remove/<int:userfollower_pk>', views.RemoveMyFollower.as_view(), name='remove-my-userfollower'),

    # APPLICATIONS
    path('offer/<int:offer_pk>/application/delete/<int:pk>', views.ApplicationDeleteView.as_view(), name='application-delete'),
    path('offer/<int:offer_pk>/application/edit/<int:pk>/', views.ApplicationEditView.as_view(), name='application-edit'),
    path('offer/<int:pk>/confirmtaken/', views.ConfirmOfferTaken.as_view(), name='confirm-offer-taken'),
    path('offer/<int:pk>/confirmgiven/', views.ConfirmOfferGiven.as_view(), name='confirm-offer-given'),

    #RATING and REVIEW
    path('rate/<int:offerpk>/<int:ratedpk>', views.RateUser.as_view(), name='rateuser'),
    path('rate/edit/<int:pk>', views.RateUserEdit.as_view(), name='rating-edit'),
    path('rate/delete/<int:pk>', views.RateUserDelete.as_view(), name='rating-delete'),




]
