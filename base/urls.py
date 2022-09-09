
from django.contrib import admin
from django.urls import path
from query import views as query_views
from query.models import Student
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',query_views.StudentView, name='student'),
    path('employee/',query_views.EmploeeView, name='employee'),
]
