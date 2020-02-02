from django.conf.urls import url
from post_app import views

app_name = 'post_app'

urlpatterns = [
    url(r'^post_test/$', views.post_test, name='post_test')
]
