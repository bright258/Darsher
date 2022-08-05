from django.contrib import admin
from .models import (
    Stores,
    Order,
    Darsher,
    Consumer,
    Commodity,
    City,
    Location,
    CustomUser,
    Country,
    OrderBid
    

) 




admin.site.register(Stores)
admin.site.register(Order)
admin.site.register(Darsher)
admin.site.register(Consumer)
admin.site.register(Commodity)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(CustomUser)
admin.site.register(Country)
admin.site.register(OrderBid)