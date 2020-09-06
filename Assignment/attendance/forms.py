from django import forms
from attendance.models import Attendance
from django.contrib.auth.models import User

PROJECT_CHOICES = [
    ('Project 1','Project 1'),
    ('Project 2','Project 2'),
    ('Project 3','Project 3'),
    ('Project 4','Project 4'),
    ('Project 5','Project 5'),
]
class AttendanceForm(forms.ModelForm):
    project_name = forms.CharField(label='Project Name',widget=forms.Select(choices=PROJECT_CHOICES), required=False)
    task_name = forms.CharField(label='Task Name', max_length=100)
    start_time = forms.DateTimeField(label='Start Time', required=True)
    end_time = forms.DateTimeField(label='End Time', required=False)
    class Meta():
        model = Attendance
        fields = ('project_name','task_name','start_time','end_time')
        