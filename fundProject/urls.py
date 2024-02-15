# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
    path('addCategory/', addCategory, name='addCategory'),
    path('delete-category/', deleteCategory, name='deleteCategory'),
    path('', mainPage, name='mainPage'),
    path('addProject/', addProject, name='addProject'),
    path('detailProject/',detailProject, name='detailProject'),

]
 

