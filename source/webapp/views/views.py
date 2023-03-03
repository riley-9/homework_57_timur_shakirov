from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from source.webapp.models.types_models import Entry
from source.webapp.forms.forms import EntryForm


def CreateTaskView(TemplateVeiw):
    template_name = 'create_task.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = EntryForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST)
        task = request.POST.get('state_type')
        if form.is_valid():
            task = form.save()
            return redirect('show_task', pk=task.pk)
        return render(request, 'create_task.html', context={'form': form})


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Entry, pk=kwargs['pk'])
        return context


class ConfirmDeleteView(RedirectView):
    def get(self, *args, **kwargs):
        task = get_object_or_404(Entry, pk=kwargs['pk'])
        task.delete()
        return redirect('show_tasks')


class TasksView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Entry.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks_to_delete = request.POST.getlist('task')
        Entry.objects.filter(pk__in=tasks_to_delete).delete()
        context['tasks'] = Entry.objects.all()
        return self.render_to_response(context)


class TaskView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class UpdateView(TemplateView):
    template_name = 'update_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Entry, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = EntryForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Entry, pk=kwargs.get('pk'))
        form = EntryForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('show_task', pk=task.pk)
        return render(request, 'update_task.html', context={'form': form})
