# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
    path('', allUser, name='allUser'),
    path('addUser/', addUser, name='addUser'),
    path('updateUser/', updateUser, name='updateUser'),
    path('insertuser/', insertuser, name='insertuser'),
    
]
 