from . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('edit_selection/', views.EditSelection.as_view(), name='edit_selection'),
    path('edit_image/<int:pk>/', views.EditImage.as_view(), name='edit_image'),
    path('sort_images/', views.sort_images, name='sort_images'),
]
