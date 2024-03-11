from django.shortcuts import render, redirect
from .models import Image
from django.views.generic import ListView, UpdateView
from .forms import EditImageForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction


class Home(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = 'images'


@method_decorator(staff_member_required, name='dispatch')
class EditSelection(ListView):
    model = Image
    template_name = 'edit_selection.html'
    context_object_name = 'images'


@method_decorator(staff_member_required, name='dispatch')
class EditImage(UpdateView):
    model = Image
    form_class = EditImageForm
    template_name = 'edit_image.html'
    success_url = '/edit_selection/'


@staff_member_required
def sort_images(request):
    if request.method == 'POST':
        form_data = request.POST
        image_ids = [item.split('_')[1] for item in form_data if item.startswith('image')]
        images_dict = {str(image_obj.pk): image_obj for image_obj in Image.objects.filter(pk__in=image_ids)}
        images_to_update = []
        for item in form_data:
            if item.startswith('image'):
                image_id = item.split('_')[1]
                new_order = str(int(form_data[item]) * 100)
                if image_id in images_dict:
                    image_instance = images_dict[image_id]
                    image_instance.order = new_order
                    images_to_update.append(image_instance)
        if images_to_update:
            with transaction.atomic():
                Image.objects.bulk_update(images_to_update, ['order'])
        return redirect('home:index')
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'sort_images.html', context)
