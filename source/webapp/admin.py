from django.contrib import admin

from bookapp.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text', 'status']
    list_filter = ['status']
    search_fields = ['author']
    fields = ['author', 'email', 'text', 'status']


admin.site.register(Entry, EntryAdmin)
