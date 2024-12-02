# from django.urls import path
# from . import views


# #urlpatterns = [ 
# #path("user", views.UserView.as_view(), name =''),
#   #  path("register", views.UserRegister.as_view(), name ='register'),
#   #  path("login", views.UserLogin.as_view(), name ='login'),
# #path("logout", views.UserLogout.as_view(), name ='logout'),
    

# ]

from django.contrib import admin
from django.urls import path
from . import views

app_name = "SignUp"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),


]


