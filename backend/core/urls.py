from django.urls import path
from .views import (

    StoresListView,
    StoresCreateView,
    RegisterView,
    LoginView,
    MakeOrderView,
    CommodityListView,
    OrderList,
    OrderView,
    BidView,
    StoreUpdateView,
    StoreView,
    DeleteStoreView
)

urlpatterns = [ 
    path('list/store/', StoresListView.as_view()),
    path('create/store/', StoresCreateView.as_view()),
    path('update/store/<int:pk>/', StoreUpdateView.as_view()),
    path('view/store/<int:pk>/', StoreView.as_view()),
    path('delete/store/<int:pk>/', DeleteStoreView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('make_order/', MakeOrderView.as_view()),
    path('list/commodity/', CommodityListView.as_view()),
    # path('create/commodity/')
    path('order_list/', OrderList.as_view()),
    path('order/<int:pk>/', OrderView.as_view()),
    path('bid_order/', BidView.as_view())
]