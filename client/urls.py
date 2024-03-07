from . import views
from django.urls import path


app_name = 'clients'
urlpatterns = [
    path('', views.AllClients.as_view(), name='clients'),
]
