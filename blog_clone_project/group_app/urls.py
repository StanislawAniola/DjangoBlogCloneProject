from django.conf.urls import url, include
from group_app import views

app_name = 'group_app'

urlpatterns = [
    url(r'^group_list/$', views.GroupListView.as_view(), name='group_list'),
    # url(r'^group_list/post_app/', include('post_app.urls', namespace='post_app')),
]
