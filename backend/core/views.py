from django.shortcuts import render
from django.urls import path
from jsonschema import ValidationError
from requests import delete


from rest_framework.parsers import MultiPartParser
from .models import (
    OrderBid,
    Stores,
    CustomUser,
    Order,
    Commodity
    )
from .serializers import (
    StoreSerializer,
   RegisterSerializer,
   MakeOrderSerializer,
   CommoditySerializer,
   TakeOrderSerializer
   
)

from rest_framework.response import Response
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    
    

    ListAPIView)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
    )

from rest_framework.response import Response
from rest_framework import status


class StoresListView(ListAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = StoreSerializer
    queryset = Stores.objects.all()

    def get(self, request, *args, **kwargs):
        stores = Stores.objects.all()
        serializer = self.serializer_class(stores, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class StoresCreateView(CreateAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = StoreSerializer
    queryset = Stores.objects.all()
    parser_classes = (MultiPartParser,)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data, context = {'request':request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)


class StoreUpdateView(UpdateAPIView):
    permission_classes = [ 
        AllowAny
    ] 
    serializer_class = StoreSerializer
    queryset = Stores.objects.all()


    def put(self, request, *args, **kwargs):
       

        instance = self.get_object()
        serializer = self.get_serializer( 
            instance , data = request.data, context = {'request':request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
       
        return Response(
            {'details':'Item succesfully updated'}, 
            status = status.HTTP_200_OK)

class StoreView(RetrieveAPIView):
    serializer_class = StoreSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = Stores.objects.all()

    def get(self, request, pk , *args, **kwargs):
        try:
            store = Stores.objects.get(pk = pk)
            serializer = self.serializer_class(store)
        except(Stores.DoesNotExist, ValidationError):
            return  Response(
                {'details':'Item not found'}, 
                status = status.HTTP_404_NOT_FOUND )
        
        return Response(
            serializer.data, status = status.HTTP_200_OK)


class DeleteStoreView(DestroyAPIView):
    serializer_class = StoreSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = Stores.objects.all()

    def delete(self, request, pk ,*args, **kwargs):
        store = Stores.objects.filter(pk = pk)
        store.delete()
       

        return Response(
            {'details':'item successfully deleted'}, status = status.HTTP_200_OK)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = CustomUser.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data, context = {'requset': request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_classes = RegisterSerializer
    queryset = CustomUser

    
    def post(self, request):
       email = request.data.get('email')
       password = request.data.get('password')
       user_data = CustomUser.objects.get(email = email)
       user = authenticate(email = email, password = password)

       return Response({
           'token': user.auth_token.key,
           'email': email,
           'username':user_data.username,
           'id': user_data.id
           
       })


class MakeOrderView(CreateAPIView):
    serializer_class = MakeOrderSerializer
    permission_classes = [  
        AllowAny
    ]
    queryset = Order

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)



class OrderList(ListAPIView):
    serializer_class = MakeOrderSerializer
    # this should not open to anyone
    permission_classes = [ 
        AllowAny


    ]
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = self.serializer_class(orders, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)


class OrderView(RetrieveAPIView):
    serializer_class = MakeOrderSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = Order.objects.all()

    def get(self, request, pk , *args, **kwargs):
        order = Order.objects.get(pk = pk)
        serializer = self.serializer_class(order)
        return Response(serializer.data, status = status.HTTP_200_OK)



class CommodityListView(ListAPIView):
    serializer_class = CommoditySerializer
    permission_classes = [

        AllowAny
    ]
    queryset = Commodity

    def get(self, request, *args, **kwargs):
        commodities = Commodity.objects.all()
        serializer = self.serializer_class(commodities, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)




class BidView(CreateAPIView):
    serializer_class = TakeOrderSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = OrderBid

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data = request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)