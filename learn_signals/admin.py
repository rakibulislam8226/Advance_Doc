from django.contrib import admin
from learn_signals import models
# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Profile)