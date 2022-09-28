from django.urls import path
from . import views


urlpatterns = [    
    path('friend-list/', views.friend_list, name='friend-list'),
    path('friend-add/', views.friend_add, name='friend-add'),
    path('add-block/', views.add_block, name='add-block'),
    path('block-list/', views.block_list, name='block-list'),
]