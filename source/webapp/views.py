from django.shortcuts import render, redirect, get_object_or_404

from source.webapp.models.types_models import Entry
from source.webapp.forms.forms import EntryForm


def index_view(request):
    if request.GET.get('author'):
        entries = Entry.objects.filter(author=request.GET.get('author'))
    else:
        entries = Entry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={'entries': entries})


def entry_create_view(request):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'create_task.html', context={'form': form})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = Entry.objects.create(
                author=form.cleaned_data.get('author'),
                email=form.cleaned_data.get('email'),
                text=form.cleaned_data.get('text')
            )
            return redirect('index')
        return render(request, 'create_task.html', context={'form': form})


def entry_update_view(request, pk):
    erors = {}
    entry = get_object_or_404(Entry, id=pk)
    if request.method == 'GET':
        form = EntryForm(initial={
            'author': entry.author,
            'email': entry.email,
            'text': entry.text,
        })
        return render(request, 'update_task.html', context={'form': form, 'entry': entry})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.author = form.cleaned_data.get('author')
            entry.email = form.cleaned_data.get('email')
            entry.text = form.cleaned_data.get('text')
            entry.save()
            return redirect('index')
        return render(request, 'entry_update', context={'form': form, 'entry': entry})


def entry_delete_view(request, pk):
    entry = get_object_or_404(Entry, id=pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', context={'entry': entry})
    elif request.method == 'POST':
        entry.delete()
        return redirect('index')
