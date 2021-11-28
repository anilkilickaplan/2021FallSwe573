from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator



class Offer(models.Model):
    offerOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    offerCreatedDate = models.DateTimeField(default=timezone.now)
    offerDescription = models.TextField()
    offerName = models.TextField()
    offerDate = models.DateTimeField(default=timezone.now)
    offerLocation = models.CharField(max_length=100, blank=True, null=True)
    offerCapacity = models.IntegerField(default=10, validators=[MinValueValidator(3),MaxValueValidator(100)])
    offerIsActive = models.BooleanField(default=True)

class Event(models.Model):
    eventOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    eventCreatedDate = models.DateTimeField(default=timezone.now)
    eventName = models.TextField()
    eventDescription = models.TextField()
    eventLocation = models.CharField(max_length=100, blank=True, null=True)
    eventDate = models.DateTimeField(default=timezone.now)
    eventCapacity = models.IntegerField()
    eventIsActive = models.BooleanField(default=True)

class Feedback(models.Model):
    feedback = models.TextField()
    createddate = models.DateTimeField(default=timezone.now)
    service = models.ForeignKey('Offer', on_delete=models.CASCADE)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile',on_delete=models.CASCADE)
    userName = models.CharField(max_length=30, blank=True, null=True)
    userBio = models.TextField(max_length=500, blank=True, null=True)
    userBirthDate = models.DateField(null=True, blank=True)
    userLocation = models.CharField(max_length=100, blank=True, null=True)
    userCredits=models.IntegerField(default=5)

#class OfferAttendees(models.Model):

#class EventAttendees(models.Model):

#class Friendship(models.Model)




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
