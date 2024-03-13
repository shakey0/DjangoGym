from . import views
from django.urls import path


app_name = 'staff'
urlpatterns = [
    path('', views.AllStaff.as_view(), name='staff'),
    path('sort/', views.sort_staff, name='sort_staff'),
    path('<int:pk>/', views.StaffDetail.as_view(), name='staff_detail'),
    path('add/', views.add_instructor, name='add_instructor'),
    path('update/<int:pk>/', views.update_instructor, name='update_instructor'),
    path('delete/<int:pk>/', views.delete_instructor, name='delete_instructor'),
]
