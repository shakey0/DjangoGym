from django.shortcuts import redirect
from .models import Scheduled
from classes.models import Class
from instructor.models import Instructor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AddScheduledForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.urls import reverse_lazy


class FullSchedule(ListView):
    model = Scheduled
    template_name = 'schedule.html'
    context_object_name = 'given_schedule'
    ordering = ['date', 'start_time']
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule_type'] = 'full'
        return context
    

@login_required
def book_class(request):
    if request.method == 'POST':
        user = request.user
        scheduled = Scheduled.objects.get(id=request.POST['scheduled_id'])
        scheduled.users.add(user)
        scheduled.save()
        return redirect('scheduled:my_schedule')
    

@login_required
def cancel_class(request):
    if request.method == 'POST':
        user = request.user
        scheduled = Scheduled.objects.get(id=request.POST['scheduled_id'])
        scheduled.users.remove(user)
        scheduled.save()
        return redirect('scheduled:my_schedule')
        

@method_decorator(login_required, name='dispatch')
class MySchedule(ListView):
    model = Scheduled
    template_name = 'schedule.html'
    context_object_name = 'given_schedule'

    def get_queryset(self):
        return Scheduled.objects.filter(users=self.request.user).order_by('date', 'start_time')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule_type'] = 'my'
        return context
    
    
class ClassSchedule(ListView):
    model = Scheduled
    template_name = 'schedule.html'
    context_object_name = 'given_schedule'
    paginate_by = 20
    
    def get_queryset(self):
        return Scheduled.objects.filter(class_id=self.kwargs['class_id']).order_by('date', 'start_time')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule_type'] = 'class'
        context['class_name'] = Class.objects.get(id=self.kwargs['class_id']).name
        return context
    
    
class InstructorSchedule(ListView):
    model = Scheduled
    template_name = 'schedule.html'
    context_object_name = 'given_schedule'
    paginate_by = 20
    
    def get_queryset(self):
        return Scheduled.objects.filter(instructor_id=self.kwargs['instructor_id']).order_by('date', 'start_time')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule_type'] = 'instructor'
        context['instructor_name'] = Instructor.objects.get(id=self.kwargs['instructor_id']).user.username
        return context


@method_decorator(staff_member_required, name='dispatch')
class AddScheduled(CreateView):
    model = Scheduled
    form_class = AddScheduledForm
    template_name = 'add_scheduled.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'{form.instance.class_id.name} class added on {form.instance.date.strftime("%d %B")} at {form.instance.start_time.strftime("%H:%M")}.')
        return response
    
    def get_success_url(self):
        return reverse_lazy('scheduled:class_schedule', kwargs={'class_id': self.object.class_id.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_add'] = True
        return context


@method_decorator(staff_member_required, name='dispatch')
class UpdateScheduled(UpdateView):
    model = Scheduled
    form_class = AddScheduledForm
    template_name = 'add_scheduled.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'{form.instance.class_id.name} class on {form.instance.date.strftime("%d %B")} at {form.instance.start_time.strftime("%H:%M")} updated.')
        return response
    
    def get_success_url(self):
        return reverse_lazy('scheduled:class_schedule', kwargs={'class_id': self.object.class_id.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_add'] = False
        return context


@method_decorator(staff_member_required, name='dispatch')
class DeleteScheduled(DeleteView):
    model = Scheduled
    template_name = 'delete_scheduled.html'
    success_url = '/scheduled/'
