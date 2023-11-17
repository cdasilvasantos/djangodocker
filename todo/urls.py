# todo/urls.py
from django.urls import path
from .views import todo_list, todo_detail, todo_create, todo_update, todo_delete

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),
    path('todo/new/', todo_create, name='todo_create'),
    path('todo/<int:pk>/edit/', todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
]
