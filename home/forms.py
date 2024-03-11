from django import forms
from .models import Image


class EditImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'desc']
        labels = {
            'desc': 'Description',
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'staff-input-width'}),
            'desc': forms.Textarea(attrs={'rows': 3, 'class': 'staff-textarea-width'}),
        }
