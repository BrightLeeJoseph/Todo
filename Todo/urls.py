"""
URL configuration for Todo project.

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
from django.urls import path
from work.views import Registration,Signin,Add_task,Delete_task,Taskedit,Signout,Del_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',Registration.as_view(),name='regis'),
    path('login/',Signin.as_view(),name='login'),
    path('task/',Add_task.as_view(),name='index'),
    path('del/<int:pk>',Delete_task.as_view(),name='delete'),
    path('up/<int:pk>',Taskedit.as_view(),name='update'),
    path('signout/',Signout.as_view(),name='logout'),
    path('delete/<int:pk>',Del_user.as_view(),name="del")



]
