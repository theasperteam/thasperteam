"""theaseperteam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from asper.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', Test),
    path('', Index, name='Index'),
    path('team/', Team, name='Team'),
    path('pillar/', Pillar, name='Pillar'),
    path('profile/', Profile, name='Profile'),
    path('signin/', SignIn, name='SignIn'),
    path('signup/', SignUp, name='SignUp'),
    path('logout/', Logout, name='logout'),
    path('firsttask/', FirstTk, name='FirstTask'),
    path('profiles/', AllProfile, name='AllProfiles'),
    path('work/', Work, name='Work'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
