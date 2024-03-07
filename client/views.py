from django.shortcuts import render, redirect
from .models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .forms import AddClassForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction


@method_decorator(staff_member_required, name='dispatch')
class AllClients(ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'
