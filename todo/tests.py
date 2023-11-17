# todo/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import TodoItem

class TodoTests(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(title='Test Todo', description='This is a test todo.')

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')

    def test_todo_detail_view(self):
        response = self.client.get(reverse('todo_detail', args=[self.todo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo_create'), {'title': 'New Todo', 'description': 'This is a new todo.'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful creation

        new_todo = TodoItem.objects.get(title='New Todo')
        self.assertEqual(new_todo.description, 'This is a new todo.')

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo_update', args=[self.todo.id]), {'title': 'Updated Todo', 'description': 'This is an updated todo.'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful update

        updated_todo = TodoItem.objects.get(id=self.todo.id)
        self.assertEqual(updated_todo.title, 'Updated Todo')
        self.assertEqual(updated_todo.description, 'This is an updated todo.')

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo_delete', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful deletion

        with self.assertRaises(TodoItem.DoesNotExist):
            TodoItem.objects.get(id=self.todo.id)
