# urls.py
from django.urls import path
from .views import addCategory, deleteCategory


urlpatterns = [
    path('addCategory/', addCategory, name='addCategory'),
    path('delete-category/', deleteCategory, name='deleteCategory'),
 
]
