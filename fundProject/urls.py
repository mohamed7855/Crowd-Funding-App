from django.urls import path
from .views import * 


urlpatterns = [
    path('', mainPage, name='mainPage'),
    path('addProject/', addProject, name='addProject'),
    path('detailProject/',detailProject, name='detailProject')

]
