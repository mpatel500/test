"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
<<<<<<< HEAD
from inventory.views import AllWebservers, AddWebserverView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webservers/', AllWebservers.as_view(), name ='all_webservers'),
    path('webservers/add_webserver', AddWebserverView.as_view(), name='add_webserver'),
=======
from inventory.views import AllWebservers, AllItems

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webservers/', AllWebservers.as_view(), name ='all-webservers'),
    path('home/', AllItems.as_view(), name ='all-items')
>>>>>>> 156fd15fb7dae9c2929daf9264cd8362f532ac7e
]
urlpatterns += staticfiles_urlpatterns()