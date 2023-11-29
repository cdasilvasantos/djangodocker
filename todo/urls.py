# todo/urls.py
from django.urls import path
from .views import todo_list, todo_detail, todo_create, todo_update, todo_delete, custom_login


urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('login/', todo_list, name='custom_login'),
    path('<int:pk>/', todo_detail, name='todo_detail'),
    path('create/', todo_create, name='todo_create'),
    path('<int:pk>/update/', todo_update, name='todo_update'),
    path('<int:pk>/delete/', todo_delete, name='todo_delete'),
]
