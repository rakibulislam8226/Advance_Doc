from django.contrib import admin
from . models import Friends, BlockFriends
# Register your models here.

admin.site.register(Friends)
admin.site.register(BlockFriends)