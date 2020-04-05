from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.auth import get_user_model
from django.http import Http404
from django.urls import reverse_lazy
# from braces.views import SelectRelatedMixin

# Create your views here.
"""
Create Post +
User Posts +
Post Detail +
Delete Post 
Post List
"""

User = get_user_model()

class AllPosts(generic.ListView):
    model = Post
    template_name = 'posts/all_posts.html'
    # select_related = ('user', 'group')


class PostForm(generic.CreateView, LoginRequiredMixin):
    model = Post
    fields = ('group', 'content')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostDetail(generic.DetailView):
    model = Post
    

class UserPosts(generic.ListView):
    """
    This is a list view to return a list of all posts by a particular user.
    
    """
    model = Post
    template_name = 'posts/user_posts.html'

    def get_queryset(self):
        # all the posts which were created by a user who's username matches that which is in the url(request)
        #? self.kwargs is a dictionary holding the request variables
        self.posts_for_user = Post.objects.filter(user__username=self.kwargs.get('username'))
        #? the above allows us to get the posts which have their user's username matching the username passed by the request
        if self.posts_for_user.count() > 0:
            return self.posts_for_user
        #? so if there's no such user it returns an empty queryset
        #? in that case we raise a 404 error
        else:
            raise Http404
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.kwargs.get('username')
        # print(context)
        return context

class PostDelete(generic.DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('posts:all')