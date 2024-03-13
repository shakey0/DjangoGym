from django.shortcuts import get_object_or_404, render, redirect
from .models import Instructor
from classes.models import Class
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm, UpdateInstructorForm, AddInstructorForClassForm
from django.core.exceptions import PermissionDenied
from django.db import transaction


class AllInstructors(ListView):
    model = Instructor
    template_name = 'instructors.html'
    context_object_name = 'instructors'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = True
        return context
    
    
class InstructorsForClass(ListView):
    model = Instructor
    template_name = 'instructors.html'
    context_object_name = 'instructors'
    
    def get_queryset(self):
        class_id = self.kwargs.get('pk')
        return Instructor.objects.filter(class_instructors__id=class_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = False
        context['class'] = get_object_or_404(Class, pk=self.kwargs.get('pk'))
        return context


class InstructorDetail(DetailView):
    model = Instructor
    template_name = 'instructor_profile.html'
    
    
@staff_member_required
def sort_instructors(request):
    if request.method == 'POST':
        form_data = request.POST
        instructor_ids = [item.split('_')[1] for item in form_data if item.startswith('instructor')]
        instructors_dict = {str(instructor_obj.pk): instructor_obj for instructor_obj in Instructor.objects.filter(pk__in=instructor_ids)}
        instructors_to_update = []
        for item in form_data:
            if item.startswith('instructor'):
                instructor_id = item.split('_')[1]
                try:
                    new_order = str(int(form_data[item]) * 100)
                except ValueError:
                    return redirect('instructors:instructors')
                if instructor_id in instructors_dict:
                    instructor_instance = instructors_dict[instructor_id]
                    instructor_instance.order = new_order
                    instructors_to_update.append(instructor_instance)
        if instructors_to_update:
            with transaction.atomic():
                Instructor.objects.bulk_update(instructors_to_update, ['order'])
        return redirect('instructors:instructors')
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors,
    }
    return render(request, 'sort_instructors.html', context)


@staff_member_required
def add_instructor(request):
    form = RegisterForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            return redirect('users:user_profile', pk=user.pk)
    return render(request, 'add_instructor.html', {'form': form, 'is_add': True})


@staff_member_required
def add_instructor_for_class(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    form = AddInstructorForClassForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(class_obj)
            return redirect('instructors:instructors_for_class', pk=class_obj.pk)
    return render(request, 'add_instructor_for_class.html', {'form': form, 'class': class_obj})


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
        return redirect('instructors:instructors')
    return render(request, 'delete_instructor.html', {'instructor': instructor})


@staff_member_required
def remove_instructor_from_class(request, pk, class_id):
    instructor = get_object_or_404(Instructor, pk=pk)
    class_obj = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        class_obj.instructors.remove(instructor)
        return redirect('instructors:instructors_for_class', pk=class_obj.pk)
    return render(request, 'remove_instructor_from_class.html', {'instructor': instructor, 'class': class_obj})
