from . import views
from django.urls import path


app_name = 'class'
urlpatterns = [
    path('', views.AllClasses.as_view(), name='classes'),
    path('add/', views.AddClass.as_view(), name='add_class'),
    path('update/<int:pk>/', views.UpdateClass.as_view(), name='update_class'),
    path('delete/<int:pk>/', views.DeleteClass.as_view(), name='delete_class'),
]
