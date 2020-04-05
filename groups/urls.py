from django.urls import path, re_path
from .views import *

app_name = 'groups'
urlpatterns = [
    path('', GroupsView.as_view(), name='list'),
    path('create/', NewGroup.as_view(), name='create'),
    re_path(r'^posts/in/(?P<slug>[-\w]+)/$', GroupDetail.as_view(), name='detail'),
    re_path(r'^join/(?P<slug>[-\w]+)/$', JoinGroup.as_view(), name='join'),
    re_path(r'^leave/(?P<slug>[-\w]+)/$', LeaveGroup.as_view(), name='leave'),
]
