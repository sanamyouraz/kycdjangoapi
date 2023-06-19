from django.contrib import admin
from api.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'email', 'dob', 'province', 'gender', 'location', 'pimage', 'rdoc']

