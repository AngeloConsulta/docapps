from django.contrib import admin
from SignUp.models import User, Profile


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'wallet', 'verified']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin) 
