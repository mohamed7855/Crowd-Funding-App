# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
    path('', allUser, name='allUser'),
    path('addUser/', addUser, name='addUser'),
    path('updateUser/<int:id>', updateUser, name='updateUser'),
    path('deleteUser/<int:id>', deleteUser, name='deleteUser'),
    path('userdetails/<int:id>', userdetails, name='userdetails'),
    
]
 