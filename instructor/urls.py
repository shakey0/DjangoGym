from . import views
from django.urls import path


app_name = 'staff'
urlpatterns = [
    path('', views.AllStaff.as_view(), name='staff'),
]
