from .models import Image
from django.views.generic import ListView


class Home(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = 'images'
