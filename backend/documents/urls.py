from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
path('dashboard/', views.dashboard, name='dashboard'),

]