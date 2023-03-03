from django.urls import path

from source.webapp.views.views import TaskView, CreateTaskView, UpdateView, DeleteView, ConfirmDeleteView

urlpatterns = [
    path('', TaskView.as_view(), name='index'),
    path('task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/<pk>/update/',UpdateView.as_view() , name='update_task'),
    path('task/<pk>/delete/', ConfirmDeleteView.as_view(), name='delete_task'),
    path('task/<pk>/', TaskView.as_view(), name='show_task'),
    path('task/<pk>/confirm-delete/', ConfirmDeleteView.as_view(permanent=True), name='confirm_delete_task')
]
