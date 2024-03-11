from .models import Image
from django.views.generic import ListView, UpdateView
from .forms import EditImageForm


class Home(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = 'images'


class EditSelection(ListView):
    model = Image
    template_name = 'edit_selection.html'
    context_object_name = 'images'


class EditImage(UpdateView):
    model = Image
    form_class = EditImageForm
    template_name = 'edit_image.html'
    success_url = '/edit_selection/'
