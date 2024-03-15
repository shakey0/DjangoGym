from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from .forms import LoginForm, UpdatePhotoForm
from django.contrib import messages


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Login success! Hi, {username}!')
                return redirect('home:index')
            else:
                messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home:index')


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
