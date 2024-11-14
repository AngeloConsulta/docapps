from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
   # email = models.EmailField(unique=True)
    #username = models.CharField(max_length=150)
    #bio = models.CharField(max_length= 100)


    #USERNAME_FIELD = 'email'
   # REQUIRED_FIELDS = ['username']

    #def __str__(self):
     #   return self.username
    # Other custom fields here
    user = models.CharField(max_length=150)  # Change 'user' to have a valid max_length


    #Override groups and user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
   )
    user_permissions = models.ManyToManyField(
Permission,
       related_name="custom_user_permissions",
       blank=True,
   )
