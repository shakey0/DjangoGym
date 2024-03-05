from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
]
