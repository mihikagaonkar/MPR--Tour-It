from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist




class PlaceType(models.Model): #tag
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name  #i.e restaurants,shopping,hotel,park etc

class Place(models.Model): #product
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=2000, null=True, blank=True)
    phone number = models.CharField(max_length=2000, null=True, blank=True)
    website = models.CharField(max_length=2000, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    placetypes = models.ForeignKey(PlaceType, null = True, on_delete =models.CASCADE)
    pic = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="/images/profile1.jpg",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    place = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return self.user.username or 'no value'

class ItineraryPlace(models.Model):
    product = models.OneToOneField(Place, on_delete=models.SET_NULL, null=True)
    is_wishlisted = models.BooleanField(default=False)

    def _str_(self):
        return self.product.name


class Itinerary(models.Model):
    ref_code = models.CharField(max_length=15,null=True)
    customer= models.ForeignKey(Customer, null=True, on_delete=models.CASCADE) #a itinerary has a foreign key of customer, if the customer is removed you delete the itinerary, one customer has many itinerary
    place= models.ManyToManyField(ItineraryPlace) #itinerary has a forieng key of place talble
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_added = models.BooleanField(default=False)

    def get_itinerary_items(self):
        return self.place.all()

    def __str__(self):
        return self.ref_code







# Create your models here.
