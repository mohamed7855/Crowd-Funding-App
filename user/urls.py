# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
    path('updateUser/', updateUser, name='updateUser'),
    path('insertuser/', insertuser, name='insertuser'),
    # path('delete-category/', deleteCategory, name='deleteCategory'),
    
]
 

