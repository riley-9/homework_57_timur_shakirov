from django import forms

from source.webapp.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['author', 'email', 'text']
