from django.urls import path
from core.views import index  # Ensure "core" is your app name and "index" is your view

app_name = "core"

urlpatterns = [
    
    path('', index, name='index'),  # Empty string for the root URL
]
 