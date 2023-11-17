# Building a Django Backend with a Database: A Comprehensive Tutorial

### Introduction
Welcome to our tutorial on building a Django backend with a database. In this step-by-step guide, we will delve into the fundamentals of Django, a high-level Python web framework renowned for its efficiency and clean design. Join us, authored by Chiara daSilva Santos, Christian Wantong, and Michael Daniels, as we explore the key components of Django development, including migrations, models, factories, seeding the database with fake data, and testing the database.

### Summary 
Django, operating on the Model-View-Controller (MVC) pattern, provides a powerful toolkit for rapid and clean web application development. This tutorial is a gateway to essential aspects of Django, serving as a foundation for developers aspiring to craft reliable and scalable web applications. By mastering Django and its associated tools such as migrations, models, factories, seeding, and testing, developers gain the skills necessary to build efficient and well-architected backend systems.

### Authors
- Chiara daSilva Santos
- Christian Wantong
- Michael Daniels

#### Attendance
[Click Here to View Our Attendance for the 2023 Fall Semester](attendance.md)

### Prerequisites
Ensure that you have the following installed on your system
- Python
- Pip (Python Package Installer)
- Django

To install Django, run the following command on terminal:
```
pip install django
```

#### Step 1: Setting up the Project
1. Create a Django Project:
```
django-admin startproject myproject
```

2. Navigate to Your Project:
```
cd my project
```

#### Step 2: Creating Migrations and Models
1. Create a Django App:
```
python manage.py startapp myapp
```
(you may need to change python to python3 depending on the version you are using)

3. Define a Model: Edit 'myapp/models.py' and run the following command:

```
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
```
3. Make Migrations:
```
python3 manage.py makemigrations
```

5. Apply Migrations:
```
python3 manage.py migrate
```

#### Step 3: Creating Factories and Seeding with Fake Data
1. Install Factory Boy:
```
pip3 install factory-boy
```

2. Define a Factory:
Create 'myapp/factories.py' and run the following command:

```
import factory
from .models import MyModel

class MyModelFactory(factory.Factory):
    class Meta:
        model = MyModel

    name = factory.Faker('word')
    description = factory.Faker('text')
```

3. Create seed.py in myapp and add the following:
```
from django.core.management.base import BaseCommand
from myapp.factories import MyModelFactory

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Seed 10 records
            MyModelFactory()
```

4. Run:
```
mkdir myapp/management
```

5. Run:
```
mkdir myapp/management/commands
```

6. Run:
```
touch myapp/management/commands/seed.py
```

7. Run:
```
python3 manage.py seed
```

#### Step 4: Testing the Database
1. Create 'myapp/tests.py' and add the following: 
```
from django.test import TestCase
from .models import MyModel

class MyModelTests(TestCase):
    def test_database(self):
        count_before = MyModel.objects.count()

        # Create a new record
        MyModel.objects.create(name='Test Name', description='Test Description')

        count_after = MyModel.objects.count()
        self.assertEqual(count_after, count_before + 1)



def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/student_list.html')


```
You are then going to create tests based on your criteria, examples being ensuring the factory works, the creation of your desired template functions, and much more. 

Example Tests can be like the following : 
```
class StudentUpdateViewTest(TestCase):
    def setUp(self):
        self.student = StudentFactory.create()

    def test_update_student(self):
        post_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com'
        }
        url = reverse('student_update', kwargs={'pk': self.student.pk})
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, 'Jane')

class StudentDeleteViewTest(TestCase):
    def setUp(self):
        self.student = StudentFactory.create()

    def test_delete_student(self):
        url = reverse('student_delete', kwargs={'pk': self.student.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Student.objects.count(), 0)

```
2. Run: To run these tests you are going to use the command below in your terminal:

```
python3 manage.py test
```

### Conclusion
You have completed the tutorial on building a Django backend with a database. You have learned how to create migrations, define modeles, use factories for fake data, seed the database, and write tests!

### Tutorial to Create a TODO Application in Django, using CSRF Tokens
[Tutorial](instructions_todo.md)
