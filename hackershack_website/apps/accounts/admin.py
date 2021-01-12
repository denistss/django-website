from django.contrib import admin

from .models import UserProfile, UserPersona, Userinterest

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(Userinterest)
