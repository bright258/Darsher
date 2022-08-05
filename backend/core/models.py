from locale import currency
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomManager

from django.conf import settings

from cloudinary.models import CloudinaryField

from .enums import (
    CountryStatus,
    OrderStatus,
    StoreStatus,
    DarsherOrderStatus,
    DarsherStatus,
    Currency,
    CommodityStatus,
    BidStatus

)

import datetime
import uuid
# import timezone


class CustomUser(AbstractUser):

    email = models.EmailField(_('email'), unique= True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomManager()


    def __str__(self):
        return str(self.email)

    

    


class Base(models.Model):
    uid = models.UUIDField(default = uuid.uuid4, null = True)
    created_at = models.DateTimeField( default = datetime.datetime.now, null = True)
    updated_at = models.DateTimeField(default = datetime.datetime.now, null = True)

    class Meta:
        abstract = True
        ordering = ('-updated_at', '-created_at')


    


class Country(Base):
    name = models.CharField(_('name'), max_length= 200, null = False, blank = True)
    
    class Meta:
        verbose_name = 'Countries'
        

    def __str__(self):
        return self.name
    


class City(Base):
    country = models.ForeignKey(Country, on_delete= models.CASCADE, related_name='country')
    name = models.CharField(_('name'), max_length= 20, null = True)
    top_city = models.BooleanField(_('top_city'), default = False)

    class Meta:
        verbose_name = 'Cities'
        
    
    def __str__(self):
        return self.name

class Location(Base):
    city = models.ForeignKey(City, on_delete= models.CASCADE, related_name= 'city')
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
   

class Stores(Base):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='stores', null = True)
    location = models.ForeignKey(Location, on_delete= models.CASCADE, related_name= 'location', null = True)
    name = models.CharField(_('name'), max_length= 200)
    status = models.CharField(
        _('status'), 
        max_length = 200, 
        default = StoreStatus.INACTIVE,
        choices = StoreStatus.choices
        )
    opening_time = models.DateTimeField(_('opening_time'), null = True)
    closing_time = models.DateTimeField(_('closing_time'), null =True)
    email = models.EmailField(_('email'),null = True)
    phone_number = models.CharField(_('phone_number'), max_length = 11 ,null = True)
    bio = models.TextField(_('bio'), null = True, max_length= 1000)
    website_url = models.URLField(_('website'),null = True)
    commodity = models.ManyToManyField('Commodity', related_name= 'commodity')

    # image = CloudinaryField('image')
    favorite = models.BooleanField(_('favourite'),default= False)
  
    @property
    def image_url(self):
        return(
            
            
            # f"https://res.cloudinary.com/dmjwzcjel/{self.image}"
        )

    def __str__(self):
        return self.name

class DarsherCompany(Base):
    name = models.CharField(_('name'),max_length = 200 )
    locations = models.ManyToManyField(Location, related_name= 'locations')
    bio = models.TextField(_('bio'),max_length = 1000, null = True)
    phone_number = models.CharField(_('phone_number'), max_length= 11, null = True )
    email = models.EmailField(_('email'), null = True)
    website_url = models.URLField(_('website'),null = True)

    def __str__(self):
        return self.name


class Commodity(Base):
    name = models.CharField(_('name'), max_length= 200, null = False)
    trending = models.BooleanField(_('trending'), default = False)
    description = models.TextField(_('description'), max_length = 500, null = False)
    image = models.ImageField(_('image'),upload_to = 'then', null = False)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places= 2, null = False)
    currency = models.CharField(
        _('currency'), 
        max_length= 3, 
        choices = Currency.choices, 
        default = Currency.NGN,
        null = False
        )
    status = models.CharField(
        _('status'), 
        max_length= 10, 
        choices = CommodityStatus.choices, 
        default = CommodityStatus.AVAILABLE,
        null = False
        
        )

    class Meta:
        verbose_name = 'Commodities'
        

    def __str__(self):
        return f'{self.name}  at {self.currency} {self.price} --> {self.status} '
       
    

class Consumer(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'consumer' )
    first_name = models.CharField(_('first_name'), max_length= 200, null = True, blank = True)
    last_name = models.CharField(_('last_name'), max_length= 200, null = True, blank = True)
    phone_number = models.CharField(_('phone'), max_length = 200, null= True)
    address = models.CharField(_('address'), max_length= 200, null = True, blank = True)

    def __str__(self):
        return str(self.user)

    


class Darsher(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'darsher' )
    first_name = models.CharField(_('first_name'), max_length= 200, null = True, blank = True)
    last_name = models.CharField(_('last_name'), max_length= 200, null = True, blank = True)
    status = models.CharField(_('status'), max_length = 200, choices = DarsherStatus.choices, null = True, default = DarsherStatus.INACTIVE)
    location = models.ForeignKey(Location, on_delete= models.CASCADE, null = True, related_name= 'darsher_location')
    company = models.ForeignKey(DarsherCompany, on_delete= models.CASCADE, related_name= 'transport_company', blank = True, null = True)
    orders = models.ManyToManyField('Order', related_name= 'orders')
    phone_number = models.CharField(_('phone_number'), max_length = 11, null = True)
    email = models.EmailField(_('email'),null = True)



    def __str__(self):
        return str(self.user)
   

class Reviews(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.DO_NOTHING, related_name= 'reviewer')
    review = models.TextField(_('reviews'), max_length = 1000)
   


class Order(Base):
    darsher = models.ForeignKey(Darsher, on_delete= models.CASCADE, related_name = "darsher", null = True)
    consumer= models.ForeignKey(Consumer, on_delete= models.CASCADE, related_name= 'consumer', null = True)
    store = models.ForeignKey(Stores, on_delete= models.SET_NULL,  related_name= 'store_involved', null = True)
    order = models.ManyToManyField(Commodity, related_name='order')
    delivery_spot = models.TextField(('delivery_spot'),max_length=  200)
    location = models.ManyToManyField(Location, related_name='customer_location')
    status_of_order = models.CharField(_('status'), choices = OrderStatus.choices, max_length = 200)
    time_arrived = models.DateTimeField(_('time_arrived'), null = True)
    reviews = models.ManyToManyField(Reviews, related_name = 'reviewss', blank = True )
    quantity = models.IntegerField(_('quantity'),default = 1, null= True)
    darsher_order_status = models.CharField(_('darsher_orders_status'),choices = DarsherOrderStatus.choices, max_length = 200, null = True, blank = True)
    
    # def TotalOrder(self):
    #     cost = self.quantity * self.order.price
    #     return cost 

class OrderBid(Base):
    darsher = models.ForeignKey(Darsher, on_delete= models.DO_NOTHING, related_name= 'darsher_bidding', null = True)
    order =  models.ForeignKey(Order, on_delete= models.DO_NOTHING, related_name= 'order_for_bidding', null = True)
    status = models.CharField(_('bid_status'),max_length= 20, choices = BidStatus.choices, default = BidStatus.UNSUCCESSFUL)

    def __str__(self):
        return f'{self.darsher} bidded for {self.order}'

class SuccessfulOrders():
    pass

class FailedOrders():
    pass
    


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(_('question'),max_length = 2000)
    answer = models.CharField(_("answer"),max_length= 2000)


    def __str__(self):
        return self.question












