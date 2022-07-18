from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomManager

from django.conf import settings


from .enums import (
    CountryStatus,
    OrderStatus,
    StoreStatus

)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomManager()

    


class Base(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Country(models.Model):
    name = models.CharField(_('name'), max_length= 200)
    # status = models.CharField(
    #     _('status'), 
    #     choices = CountryStatus.choices, 
    #     default = CountryStatus.ACTIVE,
    #     max_length= 200)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete= models.CASCADE, related_name='country')
    name = models.CharField(_('name'), max_length= 200)
    top_city = models.BooleanField(_('top'), default = False)
   

class Stores(models.Model):
    # users
    city = models.ForeignKey(City, on_delete= models.CASCADE, related_name= 'city')
    name = models.CharField(_('name'), max_length= 200)
    status = models.CharField(
        _('status'), 
        max_length = 200, 
        default = StoreStatus.ACTIVE,
        choices = StoreStatus.choices)

    image = models.ImageField(upload_to = 'then')
    favorite = models.BooleanField(default= False)
  


class Meal(models.Model):
    store = models.ForeignKey(Stores, on_delete= models.CASCADE, related_name = 'store')
    name = models.CharField(_('name'), max_length= 200)
    trending = models.BooleanField(_('trending'), default = False)
    description = models.CharField(_('description'), max_length = 500)
    image = models.ImageField(upload_to = 'then')
    price = models.DecimalField(_('price'), max_digits=10, decimal_places= 2)
    

class Consumer(Base):
    #user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'consumer' )
    first_name = models.CharField(_('first_name'), max_length= 200)
    last_name = models.CharField(_('last_name'), max_length= 200)
   

class Darsher(Base):
    # user 
    name = models.CharField()
    

class Snack(models.Model):
    store = models.ForeignKey(Meal ,on_delete = models.Cascade, related_name = 'store')
    name = models.CharField(_('name'), max_length= 200)
    description = models.CharField(_('description'), max_length= 200)
    image = models.ImageField(_('image'),upload_to = 'then')
    prices = models.DecimalField(_('price'), max_digits= 10, decimal_places= 2)


class Order(models.Model):
    darsher = models.ForeignKey()
    consumer= models.ForeignKey()
    order = models.ForeignKey()
    time_of_creation_of_order = models.DateTimeField()
    store = models.ForeignKey()
    estimated_duration_of_transit = models.TimeField()
    delivery_spot = models.CharField()
    status_of_order = models.CharField(_('status'), choices = OrderStatus.choices)
    proposed_arrival_time = models.DateTimeField()
    time_arrived = models.DateTimeField()
    reviews = models.CharField()
    










