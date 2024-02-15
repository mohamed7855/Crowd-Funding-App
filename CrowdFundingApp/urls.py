"""
URL configuration for CrowdFundingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from fundProject import  views as MainPage

urlpatterns = [
    path('admin/', admin.site.urls),

<<<<<<< HEAD
    path('', MainPage.mainPage),
    path('category/', include('fundProject.urls')) ,
    path('', include('user.urls')),
=======
    # path('', MainPage.mainPage),
    path('', include('fundProject.urls')) ,

>>>>>>> d0f8258be0e0d0476c7af31a2496f189b1ca276f
    path('',include('fundProject.urls')),
    path('user/', include('user.urls')) ,
    
    # path('',include('fundProject.urls')),

]
