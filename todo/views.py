# todo/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoForm

@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list'))
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list'))
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('todo_list'))
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
