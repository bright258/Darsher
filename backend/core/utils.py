from .enums import StoreStatus, CommodityStatus
from .models import (
    Stores,
    Order
)
import datetime
from rest_framework import serializers




time = datetime.datetime.now()

def store_active_check(store):
    if time > store.closing_time and time < store.opening_time:
        print('inactive store')
        store.status = StoreStatus.INACTIVE
    else:
        print('active store')
        store.status = StoreStatus.ACTIVE


def commodity_available_check(commodity):
    if commodity.status == CommodityStatus.SOLD_OUT:
        raise serializers.ValidationError({'detail':'This commodity is sold out'})

def darsher_bidder(darsher, order):
    if darsher.location == order.location.values('name'):
        Order.objects.update(darsher =  darsher)
        print('darsher is eligible')




'''
commodity trending check

compare user location with store location

only darshers in uYo should see Uyo orders

if darsher accepts order what happens

if another darsher accepts

if darsher accepts order, his status shoukd change





 
'''