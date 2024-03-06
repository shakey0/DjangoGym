from django import forms
from .models import Class


class AddClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'image', 'desc'] # add 'instructors' to fields
        labels = {
            'desc': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'staff-input-width'}),
            'image': forms.FileInput(attrs={'class': 'staff-input-width'}),
            'desc': forms.Textarea(attrs={'rows': 3, 'class': 'staff-textarea-width'}),
        }
