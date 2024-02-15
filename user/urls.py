# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
    path('addUser/', addUser, name='addUser'),
    path('', allUser, name='allUser'),

]
 
