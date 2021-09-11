from app.models import Doctor
from django.contrib import admin
from app.models import Doctor


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'skill']
