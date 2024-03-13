from . import views
from django.urls import path


app_name = 'scheduled'
urlpatterns = [
    path('', views.FullSchedule.as_view(), name='full_schedule'),
    path('book/', views.book_class, name='book_class'),
    path('cancel/', views.cancel_class, name='cancel_class'),
    path('my/', views.MySchedule.as_view(), name='my_schedule'),
    path('add/', views.AddScheduled.as_view(), name='add_scheduled'),
    path('update/<int:pk>/', views.UpdateScheduled.as_view(), name='update_scheduled'),
    path('delete/<int:pk>/', views.DeleteScheduled.as_view(), name='delete_scheduled'),
]
