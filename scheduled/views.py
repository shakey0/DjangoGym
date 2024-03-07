from django.shortcuts import render
from .models import Scheduled
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class FullSchedule(ListView):
    model = Scheduled
    template_name = 'full_schedule.html'
    context_object_name = 'full_schedule'
    ordering = ['start_time']
    paginate_by = 20
