from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import accounts.views as views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'thanks.html'), name = 'logout')
]
