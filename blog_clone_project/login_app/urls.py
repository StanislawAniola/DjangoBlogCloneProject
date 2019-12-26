from django.conf.urls import url
from login_app import views

app_name = 'login_app'

urlpatterns = [
    url(r'^login_user', views.login_user, name='login_user'),
]