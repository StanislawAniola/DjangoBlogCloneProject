"""blog_clone_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include

from blog_clone_project import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^index/$', views.index, name='index'),

    url(r'^register_app/', include('register_app.urls', namespace='register_app')),
    url(r'^login_app/', include('login_app.urls', namespace='login_app')),
    url(r'^blog_app/', include('blog_app.urls', namespace='blog_app')),
]
