"""personal URL Configuration

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
from blogs import views

from django.conf import settings
from blogs import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.show),

    path('blog', views.blog , name='data'),
    
    path('adminlogin', views.login),

    path('dashboard', views.dashoard),
    
    path('blogtable', views.blogtable),

    path('addblog', views.addblog),

    path('cmntstable', views.cmntstable),
    
    #path('blogs',views.blogs),
   
    #path('contact', views.contact),
    #path('recipe', views.recipe),
]
