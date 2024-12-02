# from enum import unique
# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=100)
#     bio = models.CharField(max_length=100)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)  # Optional, depending on requirements
    is_staff = models.BooleanField(default=False)  # Required if using admin
    groups = models.ManyToManyField(
        Group,
        related_name="appuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="appuser_set",
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username

