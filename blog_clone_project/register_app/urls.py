from django.conf.urls import url
from register_app import views

app_name = 'register_app'

urlpatterns = [
    url(r'^register_user/$', views.register_user, name='register_user'),
]
