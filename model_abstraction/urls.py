from django.urls import path
from model_abstraction import views
urlpatterns = [
    # path('book/',book_aggregation, name='book'),
    path('student_gub/', views.StudentGUBList.as_view()),
    path('student_gub/<int:pk>/', views.StudentGUBDetail.as_view()),
    
    path('student_diu/', views.StudentDIUList.as_view()),
    path('student_diu/<int:pk>/', views.StudentDIUDetail.as_view()),
    
    path('book_abs/', views.AbsBookList.as_view()),
    path('book_asb/<int:pk>/', views.AbsBookDetail.as_view()),
    
    path('isbn/', views.ISBNList.as_view()),
    path('isbn/<int:pk>/', views.ISBNDetail.as_view()),
    
    path('person/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),

]
