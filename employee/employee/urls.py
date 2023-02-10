"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from management import views

from management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comp',views.comp),
    path('show',views.show),
    path('edit/<str:cName>',views.edit),
    path('update/<str:cName>',views.update),
    path('delete/<str:cName>',views.delete),
    #employee path
    path('emp',views.emp),
    path('showemp',views.showemp),
    path('deleteEmp/<str:eFname>',views.deleteEmp),
    path('editemp/<str:eFname',views.editemp),
    path('updateEmp/<str:eFname>',views.updateEmp),
    #homepage path
    path('',views.home,name='home'),
    path('account/',include('django.contrib.auth.urls')),

]
