from django.conf.urls import url, include
from group_app import views

app_name = 'group_app'

urlpatterns = [
    url(r'^group_list/$', views.GroupListView.as_view(), name='group_list'),

    url(r'^group_list/group_create/$', views.GroupCreateView.as_view(), name='group_create'),
    url(r'^group_list/(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group_detail'),
    url(r'^group_list/(?P<pk>\d+)/group_update/$', views.GroupUpdateView.as_view(), name='group_update'),
    url(r'^group_list/(?P<pk>\d+)/group_delete/$', views.GroupDeleteView.as_view(), name='group_delete'),
    url(r'^group_list_draft/$', views.GroupListDraftView.as_view(), name='group_list_draft'),

    url(r'^group_list/(?P<pk>\d+)/group_publish', views.group_publish, name='group_publish'),

    url(r'^group_list/(?P<pk>\d+)/', include('post_app.urls', namespace='post_app')),
]
