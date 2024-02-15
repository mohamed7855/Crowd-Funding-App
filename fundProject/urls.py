from django.urls import path
from .views import * 


urlpatterns = [
    path('', mainPage, name='mainPage'),
    path('addCategory/', addCategory, name='addCategory'),
    path('delete-category/', deleteCategory, name='deleteCategory'),
    path('addProject/', addProject, name='addProject'),
    path('addProjectForm/', addProjectForm, name='addProjectForm'),
    path('detailProject/',detailProject, name='detailProject'),
]

