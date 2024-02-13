<<<<<<< HEAD
# urls.py
from django.urls import path
from .views import addCategory, deleteCategory


urlpatterns = [
    path('addCategory/', addCategory, name='addCategory'),
    path('delete-category/', deleteCategory, name='deleteCategory'),
 
=======
from django.urls import path
from .views import * 


urlpatterns = [
    path('', mainPage, name='mainPage'),
    path('addProject/', addProject, name='addProject'),
    path('detailProject/',detailProject, name='detailProject')

>>>>>>> 8aefb0271c49108c9d7d29ee238499395d4cbd7d
]
