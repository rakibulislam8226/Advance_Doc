
from django.contrib import admin
from django.urls import path
from model_manager import views as query_views
from model_manager.models import Student
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',query_views.StudentView, name='student'),
    path('employee/',query_views.EmploeeView, name='employee'),
]
