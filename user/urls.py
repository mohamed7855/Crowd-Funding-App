# urls.py
from django.urls import path,include
from .views import * 
from django.contrib.auth import views as auth_views
# from user import views as user_views


urlpatterns = [
    path('auth/',include('django.contrib.auth.urls')),
    path('', allUser, name='allUser'),
    path('addUser/', addUser, name='addUser'),
    path('updateUser/', updateUser, name='updateUser'),
    path('insertuser/', insertuser, name='insertuser'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
]
 