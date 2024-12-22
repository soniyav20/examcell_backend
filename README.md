Here is the content formatted as Markdown that you can paste directly into your .md file:

# Django and DRF Setup Guide

## Step 1: Install Django and Create a Project

1. Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows

2. Install Django and DRF:

pip install django
pip install djangorestframework
pip install mysqlclient  # Optional for MySQL integration
pip install markdown     # Optional for browsable API support
pip install djangofilter # Optional for API filtering


3. Create a Django project and an app:

django-admin startproject myproject
cd myproject
python manage.py startapp api


4. Update INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'api',
]




---

Step 2: Configure the Database

1. Update database settings in settings.py for MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


2. Optional: Use the default SQLite database if MySQL is not required.




---

Step 3: Create a Model

1. Define the model in api/models.py:

from django.db import models

class Employee(models.Model):
    EmpId = models.IntegerField(unique=True, null=False)
    EmpName = models.CharField(max_length=20)
    Salary = models.FloatField()
    TempEmp = models.BooleanField()
    JoinDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.EmpName


2. Register the model in api/admin.py:

from django.contrib import admin
from .models import Employee

admin.site.register(Employee)


3. Run migrations:

python manage.py makemigrations
python manage.py migrate




---

Step 4: Create a Serializer

1. Create a serializers.py file in the api app:

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'




---

Step 5: Create Views

1. Update api/views.py:

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# List all employees
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Create a new employee
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete an employee
class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'EmpId'

# Update an employee
class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'EmpId'




---

Step 6: Configure URLs

1. Create a urls.py file in the api app:

from django.urls import path
from .views import (
    EmployeeListAPIView, 
    EmployeeCreateAPIView, 
    EmployeeDeleteAPIView, 
    EmployeeUpdateAPIView
)

urlpatterns = [
    path('getemp/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('delete/<int:EmpId>/', EmployeeDeleteAPIView.as_view(), name='employee-delete'),
    path('update/<int:EmpId>/', EmployeeUpdateAPIView.as_view(), name='employee-update'),
]


2. Add the API URLs to the main urls.py:

from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]




---

Step 7: Testing

1. Run the development server:

python manage.py runserver


2. Test the endpoints in Postman or your browser:

List employees: GET http://localhost:8000/api/getemp/

Create an employee: POST http://localhost:8000/api/create/ (Send JSON data)

Update an employee: PUT http://localhost:8000/api/update/1/

Delete an employee: DELETE http://localhost:8000/api/delete/1/





---

Step 8: Create a Superuser

1. Create a superuser to access the Django admin:

python manage.py createsuperuser


2. Log in to the admin panel:

URL: http://localhost:8000/admin/




You can copy and paste this into your Markdown file. Let me know if you need further adjustments!

