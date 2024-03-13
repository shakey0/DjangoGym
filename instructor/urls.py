from . import views
from django.urls import path


app_name = 'instructors'
urlpatterns = [
    path('', views.AllInstructors.as_view(), name='instructors'),
    path('class/<int:pk>/', views.InstructorsForClass.as_view(), name='instructors_for_class'),
    path('sort/', views.sort_instructors, name='sort_instructors'),
    path('<int:pk>/', views.InstructorDetail.as_view(), name='instructor_detail'),
    path('add/', views.add_instructor, name='add_instructor'),
    path('add_for_class/<int:pk>/', views.add_instructor_for_class, name='add_instructor_for_class'),
    path('update/<int:pk>/', views.update_instructor, name='update_instructor'),
    path('delete/<int:pk>/', views.delete_instructor, name='delete_instructor'),
    path('delete_from_class/<int:pk>/<int:class_id>/', views.remove_instructor_from_class, name='delete_instructor_from_class'),
]
