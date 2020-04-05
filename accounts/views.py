from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import NewUserForm
from django.urls import reverse_lazy
# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = NewUserForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('accounts:login')

#* class Dashboard