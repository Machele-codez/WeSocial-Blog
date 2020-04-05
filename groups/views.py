from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Group
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import RedirectView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

"""
list 
group create
detail
join
leave
"""

User = get_user_model()


class GroupsView(ListView):
    model = Group
    # template_name = 'groups/group_list.html'


class NewGroup(CreateView, LoginRequiredMixin):
    model = Group
    fields = ('name', 'description')


class GroupDetail(DetailView):
    model = Group


class JoinGroup(RedirectView, LoginRequiredMixin):
    """
    we get the ```group``` from the join button as an argunment to the url using (self.kwargs)
    we get the ```user``` from the request
    then we use ```group```.members.add(```user```)
    """

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs['slug'])
        user = self.request.user
        group.members.add(user)
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('groups:detail', kwargs={'slug': self.kwargs['slug']})


class LeaveGroup(RedirectView, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        user = self.request.user
        group.members.remove(user)
        return super().get(self, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('groups:detail', kwargs={'slug': self.kwargs.get('slug')})
