# urls.py
from django.urls import path,include
from .views import * 


urlpatterns = [
    path('auth/',include('django.contrib.auth.urls')),
    path('', allUser, name='allUser'),
    path('addUser/', addUser, name='addUser'),
    path('updateUser/', updateUser, name='updateUser'),
    path('insertuser/', insertuser, name='insertuser'),
    path('register/', register, name='register'),
    
]
 