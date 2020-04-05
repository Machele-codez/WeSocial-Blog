from django.urls import path, re_path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', AllPosts.as_view(), name = 'all'),
    path('create/', PostForm.as_view(), name = 'create'),
    re_path(r'^by/(?P<username>\w+)/(?P<pk>\d+)$', PostDetail.as_view(), name = 'detail'),
    re_path(r'^by/(?P<username>\w+)/$', UserPosts.as_view(), name = 'user_posts'),
    re_path(r'^delete/(?P<pk>\d+)/$', PostDelete.as_view(), name = 'delete'),
]
