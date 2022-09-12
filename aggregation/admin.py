
from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Author)
admin.site.register(Publisher)
# admin.site.register(Book)
admin.site.register(Store)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['name','authorall','price','rating','publisher']