from django.urls import path
from learn_signals import views


urlpatterns = [
    # path('signals_home/',views.signals_home, name='signals_home'),
    path('post_list/', views.PostList.as_view()),
    path('post_list/<int:pk>/', views.PostDetail.as_view()),
]
