from rest_framework import (
    
    serializers,
    
)
from .models  import (

    Stores,
    Order,
    Darsher,
    DarsherCompany,
    Consumer,
    Commodity,
    City,
    Country,
    FrequentlyAskedQuestion,
    Location,
    CustomUser,
    OrderBid

)

from .utils import (
    darsher_bidder
)

from .enums import (

    CommodityStatus,
    StoreStatus,
    DarsherOrderStatus,
    DarsherStatus,
    OrderStatus,
    CustomerOrderStatus,
    CountryStatus,
    StoreOrderStatus
)

'''
update user profile
'''

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'password',
            
            ]
    
    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        user = CustomUser(email = email, username = username)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        print(Token.objects.get(user = user))
        
        return user


    

class MakeOrderSerializer(serializers.ModelSerializer):

    created_at = serializers.ReadOnlyField()
    status_of_order = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):

        order = validated_data['order']
        for i in order:
            if i.status == CommodityStatus.SOLD_OUT:
                raise serializers.ValidationError({'details': f'item {i.name} already sold out, please select another item'})
            
            else:
                i.save()
        
        

        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        darsher = self.context['request'].user
        order = instance['order']

        darsher_bidder(darsher,order);


        # Order.objects.update(darsher =  darsher)



        return super().update(instance, validated_data)



class TakeOrderSerializer(serializers.ModelSerializer):
    darsher = serializers.ReadOnlyField()
   

   
    class Meta:
        model = OrderBid
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        darsher = Darsher(user = user)
        darsher.save()
        
        print(darsher)
        order = validated_data['order']
        order.save()

        order_bid = OrderBid.objects.create( darsher = darsher, order = order)
        
        # order_bid.save()


        return Response(status = status.HTTP_201_CREATED, data = order_bid)


# class BidSuccessful(serializers.ModelSerializer):
#     class Meta:
#         model = Order
   

class PayForCommidity(serializers.ModelSerializer):
    pass

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'
    


class CountrySerializer(serializers.ModelSerializer):
    pass

class CitySerializer(serializers.ModelSerializer):
    pass

class LocationSerializer(serializers.ModelSerializer):
    pass

class FAQSerializer(serializers.ModelSerializer):
    pass

class UpdateDarsherProfile(serializers.ModelSerializer):
    pass

class UpdateUserProfile(serializers.ModelSerializer):
    pass

class NotifyOfOrderSerializer(serializers.ModelSerializer):
    pass




class StoreSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField()
    # image_url = serializers.ReadOnlyField()
    class Meta:
        model = Stores
        fields = '__all__'
    

    # def to_representation(self, instance):

    #     representation = super().to_representation(instance)
    #     representation.pop('image')
    #     return representation