from django.shortcuts import get_object_or_404, render, redirect
from .models import Client
from django.views.generic import ListView, DeleteView
# from .forms import AddClassForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm, UpdateClientForm


@method_decorator(staff_member_required, name='dispatch')
class AllClients(ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'
    
    def get_queryset(self):
        return Client.objects.all().order_by('id')


@staff_member_required
def add_client(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            return redirect('users:user_profile', pk=user.pk)
    return render(request, 'add_client.html', {'form': form, 'is_add': True})


@staff_member_required
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = UpdateClientForm(request.POST)
        if form.is_valid():
            user = form.save(client)
            return redirect('users:user_profile', pk=user.pk)
    else:
        initial_data = {
            'first_name': client.user.first_name,
            'last_name': client.user.last_name,
            'email': client.user.email,
            'phone': client.phone,
            'membership': client.membership,
        }
        form = UpdateClientForm(initial=initial_data)
    return render(request, 'add_client.html', {'form': form})
