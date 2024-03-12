from django.shortcuts import render, redirect
from .models import Instructor
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm, UpdateInstructorForm


class AllStaff(ListView):
    model = Instructor
    template_name = 'instructors.html'
    context_object_name = 'team'


class StaffDetail(DetailView):
    model = Instructor
    template_name = 'instructor_profile.html'


@staff_member_required
def add_instructor(request):
    form = RegisterForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            return redirect('users:user_profile', pk=user.pk)
    return render(request, 'add_instructor.html', {'form': form, 'is_add': True})
