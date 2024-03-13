from django import forms
from .models import Scheduled
from classes.models import Class
from instructor.models import Instructor
import datetime


class AddScheduledForm(forms.ModelForm):
    class_choices = [(c.id, c.name) for c in Class.objects.all()]
    selected_class = forms.ChoiceField(choices=[('', 'Select')] + class_choices, required=True, widget=forms.Select(attrs={'class': 'staff-input-width'}), label='Class')
    instructor_choices = [(i.id, i.user.username) for i in Instructor.objects.all()]
    selected_instructor = forms.ChoiceField(choices=[('', 'Select')] + instructor_choices, required=True, widget=forms.Select(attrs={'class': 'staff-input-width'}), label='Instructor')
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'staff-input-width', 'type': 'date'}))
    start_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class': 'staff-input-width', 'type': 'time'}))
    end_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class': 'staff-input-width', 'type': 'time'}))
    room = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'staff-input-width'}))
    capacity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'staff-input-width'}), min_value=1, max_value=25, initial=10)

    class Meta:
        model = Scheduled
        fields = ['selected_class', 'selected_instructor', 'date', 'start_time', 'end_time', 'room', 'capacity']

    def clean_selected_class(self):
        data = self.cleaned_data['selected_class']
        if data == '':
            raise forms.ValidationError("Please select a valid class.")
        return data
    
    def clean_selected_instructor(self):
        data = self.cleaned_data['selected_instructor']
        if data == '':
            raise forms.ValidationError("Please select a valid instructor.")
        return data
    
    def clean_date(self):
        data = self.cleaned_data['date']
        if data <= datetime.date.today():
            raise forms.ValidationError("The date must be in the future.")
        return data
    
    def clean_end_time(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time <= start_time:
            raise forms.ValidationError("The end time must be after the start time.")
        return end_time
    
    def save(self):
        scheduled_data = {
            'user': self.instance.user,
            'class_id': Class.objects.get(id=self.cleaned_data['selected_class']),
            'instructor': Instructor.objects.get(id=self.cleaned_data['selected_instructor']),
            'date': self.cleaned_data['date'],
            'start_time': self.cleaned_data['start_time'],
            'end_time': self.cleaned_data['end_time'],
            'room': self.cleaned_data['room'],
            'capacity': self.cleaned_data['capacity']
        }
        scheduled = Scheduled(**scheduled_data)
        scheduled.save()
        return scheduled
