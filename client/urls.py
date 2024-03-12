from . import views
from django.urls import path


app_name = 'clients'
urlpatterns = [
    path('', views.AllClients.as_view(), name='clients'),
    path('add_client/', views.add_client, name='add_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
]
