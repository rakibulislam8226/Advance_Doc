from django.contrib import admin
from . models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Country, CountryAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)

admin.site.register(City, CityAdmin)

class StudentListAdmin(admin.ModelAdmin):
    list_display = ("id","name", "roll","city","passby",)

admin.site.register(StudentList, StudentListAdmin)