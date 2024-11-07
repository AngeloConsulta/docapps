from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlspatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_views(template_name="Sign/login.html"),name='login'),
    path('logout/', LogoutView.as_views(next_page='login'), name = 'logout'),
   
]