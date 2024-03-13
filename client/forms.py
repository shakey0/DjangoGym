from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Client
import random, string


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'staff-input-width'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    DOB = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': ' staff-input-width', 'type': 'date'}), label='Date of Birth')
    membership = forms.ChoiceField(choices=[('', 'Select'), ('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium'), ('VIP', 'VIP')], required=True, widget=forms.Select(attrs={'class': 'staff-input-width'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with that username already exists.")
        return username

    def clean_membership(self):
        data = self.cleaned_data['membership']
        if data == '':
            raise ValidationError("Please select a valid membership option.")
        return data
    
    def save(self):
        # Create User instance
        user_data = {
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'username': self.cleaned_data['username'],
            'email': self.cleaned_data['email']
        }
        user = User.objects.create_user(**user_data)
        user.set_unusable_password()  # If the password is to be set by the user later
        user.save()

        # Create Client instance
        entry_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        client_data = {
            'phone': self.cleaned_data['phone'],
            'DOB': self.cleaned_data['DOB'],
            'membership': self.cleaned_data['membership'],
            'entry_code': entry_code,
            'user': user
        }
        client = Client(**client_data)
        client.save()
        
        return user


class UpdateClientForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'staff-input-width'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    membership = forms.ChoiceField(choices=[('', 'Select'), ('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium'), ('VIP', 'VIP')], required=True, widget=forms.Select(attrs={'class': 'staff-input-width'}))
    
    def clean_membership(self):
        data = self.cleaned_data['membership']
        if data == '':
            raise ValidationError("Please select a valid membership option.")
        return data
    
    def save(self, client):
        # Assume the client is passed as an argument to this method after being retrieved by pk in the view
        user = client.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        
        client.phone = self.cleaned_data['phone']
        client.membership = self.cleaned_data['membership']
        client.save()
        
        return user
