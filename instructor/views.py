from django.shortcuts import render, redirect
from .models import Instructor
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .forms import AddClassForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction


class AllStaff(ListView):
    model = Instructor
    template_name = 'instructors.html'
    context_object_name = 'team'


class StaffDetail(DetailView):
    model = Instructor
    template_name = 'instructor_profile.html'
