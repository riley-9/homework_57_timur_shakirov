from django import forms
from django.forms import TextInput

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'state']
        widgets = {
            'summary': TextInput(attrs={
                'class': "form-control m-75"
            }),
            'description': TextInput(attrs={
                'class': 'form-control m-75'
            }),
            'task_type': TextInput(attrs={
                'class': 'form-control m-75'
            }),
            'state_type': TextInput(attrs={
                'class': 'form-control m-75'
            })
        }
