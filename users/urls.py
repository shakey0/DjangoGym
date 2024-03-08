from . import views
from django.urls import path


app_name = 'users'
urlpatterns = [
    path('<int:pk>/', views.UserProfile.as_view(), name='user_profile'),
]
