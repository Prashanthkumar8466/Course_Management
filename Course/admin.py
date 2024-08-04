from django.contrib import admin
from .models import Course,enroll_details
@admin.register(Course,enroll_details)
class Admin(admin.ModelAdmin):
    list_display = ['id']
