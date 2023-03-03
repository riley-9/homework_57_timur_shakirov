from django.urls import path

from .views import index_view, entry_create_view, entry_update_view, entry_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('create/', entry_create_view, name='entry_create'),
    path('<int:pk>/update/', entry_update_view, name='entry_update'),
    path('<int:pk>/delete/', entry_delete_view, name='entry_delete'),
]
