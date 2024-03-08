from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'
    
    def test_func(self):
        user = self.get_object()
        return self.request.user.is_staff or self.request.user == user
    
    def handle_no_permission(self):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_user_profile'] = True
    #     return context
