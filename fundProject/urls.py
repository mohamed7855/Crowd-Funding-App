from django.urls import path
from .views import * 


urlpatterns = [
    path('', mainPage, name='mainPage'),
    path('addProject/', addProject, name='addProject'),
    path('addProjectForm/', addProjectForm, name='addProjectForm'),
    path('detailProject/',detailProject, name='detailProject')

]
