from . import views
from django.urls import path


app_name = 'scheduled'
urlpatterns = [
    path('', views.FullSchedule.as_view(), name='full_schedule'),
    path('add/', views.AddScheduled.as_view(), name='add_scheduled'),
]
