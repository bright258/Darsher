from django.db.models import TextChoices


class CountryStatus(TextChoices):
    ACTIVE = 'ACTIVE'
    COMINGSOON = 'COMING SOON'
    INACTIVE = 'INACTIVE'


class StoreStatus(TextChoices):
    ACTIVE = 'Delivering now!'
    COMINGSOON = 'Coming soon'
    SOON = 'Delivering in 10 min'

class OrderStatus(TextChoices):
    OUT = 'Out for delivery'
    CLOSEBY = 'Close by'
    ARRIVED = 'Order has arrived'
    SUCCESSFUL = 'Order was successful'