from django.urls import path
from SignUp import views
#from django.contrib.auth.views import LoginView, LogoutView


app_name = "SignUp"

urlpatterns = [ 
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    #path('signup/', views.signup, name='signup'),
#path('login/', LoginView.as_views(template_name="Sign/login.html"),name='login'),
   # path('logout/', LogoutView.as_views(next_page='login'), name = 'logout'),
   
]