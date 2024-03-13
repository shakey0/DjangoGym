from django.shortcuts import render, redirect
from .models import Class
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AddClassForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction


class AllClasses(ListView):
    model = Class
    template_name = 'classes.html'
    context_object_name = 'classes'
    

@staff_member_required
def sort_classes(request):
    if request.method == 'POST':
        form_data = request.POST
        class_ids = [item.split('_')[1] for item in form_data if item.startswith('class')]
        classes_dict = {str(class_obj.pk): class_obj for class_obj in Class.objects.filter(pk__in=class_ids)}
        classes_to_update = []
        for item in form_data:
            if item.startswith('class'):
                class_id = item.split('_')[1]
                try:
                    new_order = str(int(form_data[item]) * 100)
                except ValueError:
                    return redirect('classes:classes')
                if class_id in classes_dict:
                    class_instance = classes_dict[class_id]
                    class_instance.order = new_order
                    classes_to_update.append(class_instance)
        if classes_to_update:
            with transaction.atomic():
                Class.objects.bulk_update(classes_to_update, ['order'])
        return redirect('classes:classes')
    classes = Class.objects.all()
    context = {
        'classes': classes,
    }
    return render(request, 'sort_classes.html', context)


@method_decorator(staff_member_required, name='dispatch')
class AddClass(CreateView):
    model = Class
    form_class = AddClassForm
    template_name = 'add_class.html'
    success_url = '/classes/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_add'] = True
        return context


@method_decorator(staff_member_required, name='dispatch')
class UpdateClass(UpdateView):
    model = Class
    form_class = AddClassForm
    template_name = 'add_class.html'
    success_url = '/classes/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_add'] = False
        return context


@method_decorator(staff_member_required, name='dispatch')
class DeleteClass(DeleteView):
    model = Class
    template_name = 'delete_class.html'
    success_url = '/classes/'
    # !!! Will be dependent on all associated sessions being deleted first
