from django.shortcuts import render
from django.urls import path

from .models import StoresList
from .serializers import StoresListSerializer



from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView, 
    DestroyAPIView, 
    UpdateAPIView,

    ListAPIView)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
    )



class StoresListView(ListAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = StoresListSerializer
    # queryset = Stores


    






