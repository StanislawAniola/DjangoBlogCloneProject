from django.conf.urls import url
from post_app import views

app_name = 'post_app'

urlpatterns = [
    url(r'^post_add/$', views.post_add, name='post_add'),
    url(r'^post_publish/$', views.post_publish, name='post_publish'),
    url(r'^post_delete/$', views.post_delete, name='post_delete'),
]
