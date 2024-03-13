from . import views
from django.urls import path


app_name = 'instructors'
urlpatterns = [
    path('', views.AllInstructors.as_view(), name='instructors'),
    path('sort/', views.sort_instructors, name='sort_instructors'),
    path('<int:pk>/', views.InstructorDetail.as_view(), name='instructor_detail'),
    path('add/', views.add_instructor, name='add_instructor'),
    path('update/<int:pk>/', views.update_instructor, name='update_instructor'),
    path('delete/<int:pk>/', views.delete_instructor, name='delete_instructor'),
]
