from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from instructor.models import Instructor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UpdatePhotoForm


class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'v_user'
    
    def test_func(self):
        user = self.get_object()
        return self.request.user.is_staff or self.request.user == user
    
    def handle_no_permission(self):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_photo_form'] = UpdatePhotoForm()
        return context


@staff_member_required
def update_photo(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UpdatePhotoForm(request.POST, request.FILES, instance=user.instructor)
        if form.is_valid():
            form.save()
    return redirect('users:user_profile', pk=pk)
