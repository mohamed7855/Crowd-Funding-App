# urls.py
from django.urls import path,include
from .views import * 
from django.contrib.auth import views as auth_views
# from user import views as user_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('auth/',include('django.contrib.auth.urls')),
    path('', allUser, name='allUser'),
    path('addUser/', addUser, name='addUser'),
    path('updateUser/', updateUser, name='updateUser'),
    path('insertuser/', insertuser, name='insertuser'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('Delete/<int:user_id>/',DeleteAccount,name='DeleteAccount'),
    # path('delete_confirmation/<int:user_id>/', views.delete_confirmation, name='delete_confirmation'),
    # path('update/<int:user_id>/', views.updateUser, name='update_user'),
    # path('accounts/activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    
]
 