from . import views
from django.urls import path


app_name = 'class'
urlpatterns = [
    path('', views.AllClasses.as_view(), name='classes'),
    path('add/', views.AddClass.as_view(), name='add_class'),
]
