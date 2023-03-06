from django.urls import path

from webapp.views.views import UpdateView, ConfirmDeleteView, ListView, TaskView, CreateView, DeleteView

urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('task/create/', CreateView.as_view(), name='create_task'),
    path('task/<int:pk>/update/', UpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', ConfirmDeleteView.as_view(), name='delete_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='show_task'),
    path('task/<int:pk>/confirm-delete/', ConfirmDeleteView.as_view(permanent=True), name='confirm_delete_task'),
    path('task/<int:pk>/delete/', DeleteView.as_view(), name='delete_task'),
]
