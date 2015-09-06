from django.contrib import admin
from authentication.models import UserProfile

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'email')

admin.site.register(UserProfile)
