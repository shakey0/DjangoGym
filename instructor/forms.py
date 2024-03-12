from django import forms
from django.contrib.auth.models import User
from .models import Instructor
import random, string, json


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'staff-input-width'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    DOB = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': ' staff-input-width', 'type': 'date'}), label='Date of Birth')
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'staff-input-width'}), label='Profile Picture')
    instr_type = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}), label='Instructor Type')
    desc = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'staff-input-width'}), label='Description')
    qualifications_input = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'staff-input-width'}), label='Qualifications', help_text='Enter qualifications and separate each of them with a comma (,)')
    activities_input = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'staff-input-width'}), label='Activities', help_text='Enter activities and separate each of them with a comma (,)')
    
    def clean_qualifications_input(self):
        input_data = self.cleaned_data['qualifications_input']
        qualifications_list = [item.strip() for item in input_data.split(',')]
        return qualifications_list

    def clean_activities_input(self):
        input_data = self.cleaned_data['activities_input']
        activities_list = [item.strip() for item in input_data.split(',')]
        return activities_list
    
    def save(self):
        # Create User instance
        user_data = {
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'username': self.cleaned_data['username'],
            'email': self.cleaned_data['email'],
            'is_staff': True
        }
        user = User.objects.create_user(**user_data)
        user.set_unusable_password()  # If the password is to be set by the user later
        user.save()

        # Create Instructor instance
        entry_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        instructor_data = {
            'phone': self.cleaned_data['phone'],
            'DOB': self.cleaned_data['DOB'],
            'image': self.cleaned_data['image'],
            'instr_type': self.cleaned_data['instr_type'],
            'desc': self.cleaned_data['desc'],
            'qualifications': self.cleaned_data['qualifications_input'],
            'activities': self.cleaned_data['activities_input'],
            'entry_code': entry_code,
            'user': user
        }
        client = Instructor(**instructor_data)
        client.save()
        
        return user


class UpdateInstructorForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'staff-input-width'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    instr_type = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}), label='Instructor Type')
    desc = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'staff-input-width'}), label='Description')
    qualifications_input = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'staff-input-width'}), label='Qualifications', help_text='Enter qualifications and separate each of them with a comma (,)')
    activities_input = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'staff-input-width'}), label='Activities', help_text='Enter activities and separate each of them with a comma (,)')
    
    def clean_qualifications_input(self):
        input_data = self.cleaned_data['qualifications_input']
        qualifications_list = [item.strip() for item in input_data.split(',')]
        return qualifications_list

    def clean_activities_input(self):
        input_data = self.cleaned_data['activities_input']
        activities_list = [item.strip() for item in input_data.split(',')]
        return activities_list
    
    def save(self, instructor):
        # Assume the client is passed as an argument to this method after being retrieved by pk in the view
        user = instructor.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        
        instructor.phone = self.cleaned_data['phone']
        instructor.instr_type = self.cleaned_data['instr_type']
        instructor.desc = self.cleaned_data['desc']
        instructor.qualifications = self.cleaned_data['qualifications_input']
        instructor.activities = self.cleaned_data['activities_input']
        instructor.save()
        
        return user
