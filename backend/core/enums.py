from django.db.models import TextChoices


class CountryStatus(TextChoices):
    ACTIVE = 'ACTIVE'
    COMINGSOON = 'COMING SOON'
    INACTIVE = 'INACTIVE'


class StoreStatus(TextChoices):
    ACTIVE = 'Delivering now!'
    COMINGSOON = 'Coming soon'
    SOON = 'Delivering in 10 min'
    INACTIVE = 'Not active'

class OrderStatus(TextChoices):
    OUT = 'Out for delivery'
    CLOSEBY = 'Close by'
    ARRIVED = 'Order has arrived'
    SUCCESSFUL = 'Order was successful'


class DarsherStatus(TextChoices):
    DELIVERING = 'Curretly delievering an order'
    NOT_DELIVERING = 'Free'
    INACTIVE = 'inactive'

class StoreOrderStatus(TextChoices):
    PREPARING = 'Order is been prepared'
    SHIPPED = 'Order has been shipped'
    OUT_OF_STOCK = 'Order is out of stock'
    NO_DARSHER = 'No darsher available for this order'
    READY = 'Order is ready to be shipped'
    NOT_READY = 'Order is not ready to be shipped'


class DarsherOrderStatus(TextChoices):
    ACCEPT = 'ACCEPTED'
    REJECT = 'REJECTED'
    

class CustomerOrderStatus(TextChoices):
    RECEIVED = 'RECEIVED'
    BAD_CONDITION = 'Order in bad condition'
    NOT_RECEIVED = 'Not Received'

class Currency(TextChoices):
    NGN = 'NGN'
    USD = 'USD'
    CND = 'CND'

class CommodityStatus(TextChoices):
    AVAILABLE = 'Available'
    SOLD_OUT = 'Sold out'

class BidStatus(TextChoices):
    SUCCESSFUL = 'BID SUCCESSFUL'
    UNSUCCESSFUL = 'BID NOT SUCCESSFUL'