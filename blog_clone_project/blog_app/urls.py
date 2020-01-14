from django.conf.urls import url
from blog_app import views

app_name = 'blog_app'


urlpatterns = [
    url(r'^post_list/$', views.PostListView.as_view(), name='post_list'),

    url(r'^post_list_draft/$', views.PostListDraftView.as_view(), name='post_list_draft'),
    url(r'^post_list/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post_list/post_create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^post_list/(?P<pk>\d+)/post_detail/$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^post_list/(?P<pk>\d+)/post_delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^post_list_draft/(?P<pk>\d+)/post_publish/$', views.post_publish, name='post_publish'),

    url(r'^post_list/(?P<pk>\d+)/add_comment/$', views.comment_add, name='add_comment'),
    url(r'^post_list/(?P<pk>\d+)/comment_approve/$', views.comment_approve, name='comment_approve'),
    url(r'^post_list/(?P<pk>\d+)/comment_delete/$', views.comment_delete, name='comment_delete'),

    url(r'^test/$', views.test, name='test'),

]
