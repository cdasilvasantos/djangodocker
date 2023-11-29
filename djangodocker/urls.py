# djangodocker/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from todo.views import custom_login, custom_logout, todo_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Django authentication views
    path('login/', todo_list, name='custom_login'),  # Your custom login view
    path('logout/', todo_list, name='custom_logout'),    
    path('todo/', include('todo.urls')),
    re_path(r'^$', RedirectView.as_view(url='/todo/', permanent=True)),  # Redirect empty path to TODO app
]
