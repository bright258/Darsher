from django.urls import path
from .views import (

    StoresListView
)

urlpatterns = [ 
    path('stores/', StoresListView)
]