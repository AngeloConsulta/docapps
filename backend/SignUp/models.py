from django.db import models
from django.contrib.auth.models import User

class YourModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set a specific user ID (e.g., 1 for the first user)
