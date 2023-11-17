# Django TODO Application Tutorial

This tutorial will guide you through the process of creating a simple TODO application using Django. The application will allow you to manage a list of TODO items, including the ability to add, view, edit, and delete items.

## Step 1: Project Setup

1. Create a new Django project:

    ```terminal
    django-admin startproject djangodocker
    ```

2. Create a new app within the project:

    ```terminal
    cd djangodocker
    python manage.py startapp todo
    ```

## Step 2: Model and Database Setup

1. Define the `TodoItem` model in the `todo/models.py` file:

    ```python
    # todo/models.py
    from django.db import models
    
    class TodoItem(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
    ```

2. Run migrations to apply the model changes:

    ```terminal
    python manage.py makemigrations
    python manage.py migrate
    ```

## Step 3: Create CRUD Views

1. Create CRUD views in the `todo/views.py` file.

2. Add URL patterns in the `todo/urls.py` file.

3. Include the app's URLs in the project's `urls.py` file.

## Step 4: Templates and Styling

1. Create HTML templates in the `todo/templates/todo/` directory. In each one of these HTML files, ensure you have '{% load static %}' above the HTML code.

    - `todo_list.html`: Display a list of TODO items.
    - `todo_detail.html`: Show details of a single TODO item.
    - `todo_form.html`: Form to add or edit TODO items.
    - `todo_confirm_delete.html`: Confirmation for deleting a TODO item.

2. Style the application using CSS. Create a `style.css` file in `todo/static/todo/`. After this, ensure you add the following link to all the HTML files, '<link rel="stylesheet" type="text/css" href="{% static 'todo/style.css' %}">'

## Step 5: Test CRUD Operations

1. Write tests for CRUD operations in the `todo/tests.py` file.

2. Run tests using:

    ```terminal
    python manage.py test todo
    ```

## Step 6: Run the Application Locally

1. Start the development server:

    ```terminal
    python manage.py runserver
    ```

2. Access the application in your web browser at [http://localhost:8000/todo/](http://localhost:8000/todo/).

## Step 7: Summary of Changes

Review the changes made to various files, including models, views, URLs, templates, and styles, as described in the tutorial.

