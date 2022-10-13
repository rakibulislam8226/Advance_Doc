from django.urls import path
from . import views


urlpatterns = [    
    path('friend-list/', views.friend_list, name='friend-list'),
    path('friend-add/', views.friend_add, name='friend-add'),
    path('add-block/', views.add_block, name='add-block'),
    path('block-list/', views.block_list, name='block-list'),
    path('message-list/', views.MessageList.as_view(),name='message-list'),
    path('message-detail/<str:sender>/', views.MessageDetail.as_view(),name='message-detail'),
    
    path('group-message-list/', views.GroupMessageList.as_view(),name='group-message-list'),
    path('group-message-detail/<str:sender>/', views.GroupMessageDetail.as_view(),name='group-message-detail'),
]