# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

@login_required
def todo_list(request):
    user_greeting = f"Hello, {request.user.username}!"  # Greeting message
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'user_greeting': user_greeting, 'todos': todos})


@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})

@login_required
def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, user=request.user)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('todo_list')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'registration/login.html')

def custom_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('todo_list')  # Redirect to your custom login view
