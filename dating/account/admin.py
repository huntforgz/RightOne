from django.contrib import admin

# Register your models here.
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    #list_display = ['user', 'date_of_birth', 'photo']
    list_display = ['user','nickname','intro','photo','age','height','weight','gender','education','only_child','location']
admin.site.register(Profile, ProfileAdmin)
