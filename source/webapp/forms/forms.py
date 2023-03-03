from django import forms
from django.forms import TextInput

from source.webapp.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['summary', 'description', 'type', 'state']
        widgets = {
            'summary': TextInput(attrs={
                'class': "form-control m-75"
            }),
            'description': TextInput(attrs={
                'class': 'form-control m-75'
            }),
            'type': TextInput(attrs={
                'class': 'form-control m-75'
            }),
            'state': TextInput(attrs={
                'class': 'form-control m-75'
            })

        }
