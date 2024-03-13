from django.shortcuts import render
from .models import Scheduled
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AddScheduledForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class FullSchedule(ListView):
    model = Scheduled
    template_name = 'full_schedule.html'
    context_object_name = 'full_schedule'
    ordering = ['start_time']
    paginate_by = 20


@method_decorator(staff_member_required, name='dispatch')
class AddScheduled(CreateView):
    model = Scheduled
    form_class = AddScheduledForm
    template_name = 'add_scheduled.html'
    success_url = '/scheduled/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_add'] = True
        return context


@method_decorator(staff_member_required, name='dispatch')
class UpdateScheduled(UpdateView):
    model = Scheduled
    form_class = AddScheduledForm
    template_name = 'add_scheduled.html'
    success_url = '/scheduled/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_add'] = False
        return context


@method_decorator(staff_member_required, name='dispatch')
class DeleteScheduled(DeleteView):
    model = Scheduled
    template_name = 'delete_scheduled.html'
    success_url = '/scheduled/'
