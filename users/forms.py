from django import forms
from instructor.models import Instructor


class UpdatePhotoForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['image']
        labels = {
            'image': 'Update Profile Picture'
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control mt-1', 'accept': 'image/*'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'staff-input-width', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'staff-input-width', 'placeholder': 'Enter password'}))
