from .models import Class
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AddClassForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class AllClasses(ListView):
    model = Class
    template_name = 'classes.html'
    context_object_name = 'classes'


@method_decorator(staff_member_required, name='dispatch')
class AddClass(CreateView):
    model = Class
    form_class = AddClassForm
    template_name = 'add_class.html'
    success_url = '/classes/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
