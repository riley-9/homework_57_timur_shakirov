from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView

from webapp.forms.forms import TaskForm
from webapp.models import Task


class CreateView(TemplateView):
    template_name = 'create_task.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = TaskForm
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            states = form.cleaned_data.pop('state')
            task = form.save()
            task.type.set(types)
            task.state.set(states)
            return redirect('show_task', pk=task.pk)
        return render(request, self.template_name, context={'form': form})


class UpdateView(TemplateView):
    template_name = 'update_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        context['form'] = TaskForm(instance=task)
        context['task'] = task
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST, instance=self.get_context_data().get('task'))
        if form.is_valid():
            print('valid')
            types = form.cleaned_data.pop('type')
            states = form.cleaned_data.pop('state')
            task = form.save()
            task.type.set(types)
            task.state.set(states)
            return redirect('show_task', pk=task.pk)
        return render(request, self.template_name, context={'form': form})


class DeleteView(TemplateView):
    template_name = 'delete_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ConfirmDeleteView(RedirectView):
    def get(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('show_task')


class ListView(TemplateView):
    template_name = 'all_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks_to_delete = request.POST.getlist('task')
        Task.objects.filter(pk__in=tasks_to_delete).delete()
        context['tasks'] = Task.objects.all()
        return self.render_to_response(context)


class TaskView(TemplateView):
    template_name = 'detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['task'] = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return context

