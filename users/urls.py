from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
]