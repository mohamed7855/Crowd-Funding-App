from django.urls import path
from . import views 


urlpatterns = [

    path('',views.projectList,name="project.all"),
    path('projectlist/',views.projectList,name="project.all"),
    path('<int:projectid>',views.projectDetails,name="projectDetails"),
    path('New',views.addProject,name="projectAdd"),
    path('Delete/<int:id>',views.projectDelete,name="project.delete"),
    path('Update/<int:id>',views.projectUpdate,name="project.update"),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('allCategory/', views.allCategory, name='allCategory'),
    path('delete-category/', views.deleteCategory, name='deleteCategory'),
    path('add_rate/<int:project_id>/', views.add_rate, name='add_rate'),
    path('add_donate/<int:project_id>/', views.add_donate, name='add_donate'),
    path('comment/<int:id>',views.comment,name="comment"),    
    path('comment/<int:id>/delete/<int:comment_id>/', views.CommentDelete, name='CommentDelete'),
    path('search/', views.search_projects, name='search_projects'),

]

# path('', mainPage, name='mainPage'),
    # path('addProject/', addProject, name='addProject'),
    # path('detailProject/',detailProject, name='detailProject'),
    # path('projectList/<int:id>/', projectList),
    # path('projectDetails/<int:id>/', projectDetails),
    # path('addCommentOnProject/<int:id>/', addCommentOnProject),
    # path('reportComment/<int:id>/', reportComment),
    # path('cancelProject/<int:id>/', cancelProject),