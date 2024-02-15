# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
<<<<<<< HEAD
    path('updateUser/', updateUser, name='updateUser'),
    path('insertuser/', insertuser, name='insertuser'),
    # path('delete-category/', deleteCategory, name='deleteCategory'),
    
]
 

=======
    path('addUser/', addUser, name='addUser'),
    path('', allUser, name='allUser'),

]
 
>>>>>>> d0f8258be0e0d0476c7af31a2496f189b1ca276f
