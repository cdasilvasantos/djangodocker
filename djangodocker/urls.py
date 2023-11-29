# djangodocker/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/', include('todo.urls')),
    re_path(r'^$', RedirectView.as_view(url='/todo/', permanent=True)),  # Redirect empty path to TODO app
]
