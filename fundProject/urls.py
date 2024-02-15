# urls.py
from django.urls import path
from .views import * 


urlpatterns = [
    
        path('addCategory/', addCategory, name='addCategory'),
        path('delete-category/', deleteCategory, name='deleteCategory'),
        path('', mainPage, name='mainPage'),
        path('addProject/', addProject, name='addProject'),
        path('detailProject/',detailProject, name='detailProject'),
        # path('projectList/', projectList),
        path('projectList/<int:id>/', projectList),
        path('projectDetails/<int:id>/', projectDetails),
        path('addCommentOnProject/<int:id>/', addCommentOnProject),
        path('reportComment/<int:id>/', reportComment),
        path('cancelProject/<int:id>/', cancelProject),
    
]
 

