from django.shortcuts import get_object_or_404, render, redirect
from .models import Instructor
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm, UpdateInstructorForm
from django.core.exceptions import PermissionDenied


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


@staff_member_required
def update_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = UpdateInstructorForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(instructor)
            return redirect('users:user_profile', pk=user.pk)
    else:
        qualifications = ', '.join(instructor.qualifications)
        activities = ', '.join(instructor.activities)
        initial_data = {
            'first_name': instructor.user.first_name,
            'last_name': instructor.user.last_name,
            'email': instructor.user.email,
            'phone': instructor.phone,
            'instr_type': instructor.instr_type,
            'desc': instructor.desc,
            'qualifications_input': qualifications,
            'activities_input': activities
        }
        form = UpdateInstructorForm(initial=initial_data)
    return render(request, 'add_instructor.html', {'form': form, 'is_add': False, 'instructor': instructor})


def superuser_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

@superuser_required
def delete_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.user.delete()
        return redirect('staff:staff')
    return render(request, 'delete_instructor.html', {'instructor': instructor})
