from django.shortcuts import render, redirect
from .models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .forms import AddClassForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from .forms import RegisterForm


@method_decorator(staff_member_required, name='dispatch')
class AllClients(ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'


@staff_member_required
def AddClient(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('clients:clients')
    return render(request, 'add_client.html', {'form': form})
