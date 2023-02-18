from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Student)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
  # list_display = ['school', 'name']
  pass