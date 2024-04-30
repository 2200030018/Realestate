from django.urls import *
from .views import *

urlpatterns = [
    path('',base,name='base'),
    path('login',login,name='login'),
    path('home',home,name='home'),
    path('about',about,name='about'),
    path('signup',signup,name='signup'),
    path('sell',sell,name='sell'),
    path('buy',buy,name='buy'),
    path('property1',property1,name='property1'),
    path('property2', property2, name='property2'),
    path('property3', property3, name='property3'),
    path('property4', property4, name='property4'),
    path('buyers',buyers,name='buyers'),





]