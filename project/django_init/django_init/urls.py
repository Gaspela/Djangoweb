"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from aplicaciones.principal.views import init, createUser, editUser, delteUser
from aplicaciones.principal.classviews import UserList,CreateUser,UpdateUser,DeleteUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserList.as_view(), name='index'),
    path('createuser/', CreateUser.as_view(), name='createuser'),
    path('edituser/<int:pk>/', UpdateUser.as_view(), name='edituser'),
    path('deleteuser/<int:pk>/', DeleteUser.as_view(), name='deleteuser')
]
