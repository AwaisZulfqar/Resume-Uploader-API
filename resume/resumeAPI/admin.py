from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=['id','name',]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','pimage','doc',]
