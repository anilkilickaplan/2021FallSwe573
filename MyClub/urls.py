from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path('home', views.home, name='home'),
    # OFFER RELATED
    path('offer', views.OfferListView.as_view(), name='offer-list'),
    path('offer/<int:pk>', views.OfferDetailView.as_view(), name='offer-detail'),
    path('offer/edit/<int:pk>', views.OfferEditView.as_view(), name='offer-edit'),
    path('offer/delete/<int:pk>', views.OfferDeleteView.as_view(), name='offer-delete'),
    #path('offer/create_offer', views.OfferListView.as_view(), name='offer-create'),

    # EVENT RELATED
    path('event', views.EventListView.as_view(), name='event-list'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('event/edit/<int:pk>', views.EventEditView.as_view(), name='event-edit'),
    path('event/delete/<int:pk>', views.EventDeleteView.as_view(), name='event-delete'),
    #path('event/create_event?submitted=', views.EventListView.as_view(), name='event-create'),


    # PROFILE RELATED
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', views.ProfileEditView.as_view(), name='profile-edit'),
   
    path('myoffers/<int:pk>', views.myOffersView.as_view(), name='myoffers-list'),
    path('myevents/<int:pk>', views.myEventsView.as_view(), name='myevents-list'),


]
