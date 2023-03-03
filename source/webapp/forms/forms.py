from django import forms
from django.forms import TextInput

from source.webapp.models.types_models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['summary', 'description', 'task_type', 'state_type']
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
