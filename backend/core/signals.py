from django.db.models.signals import (
    post_save,
    pre_save
    )
from django.dispatch import receiver
from .serializers import MakeOrderSerializer
from .models import (
    Order,
    OrderBid 

    )



@receiver(post_save, sender = OrderBid )
def bid(sender, **kwargs):
    print('a darsher just bidded')


@receiver(post_save, sender = Order)
def order(sender,instance, **kwargs ):
    print('an order was just made')
    # print(instance['quantity'])
    print(instance.quantity )
    print(instance.order.all())