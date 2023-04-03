from django.contrib import admin

from .models import department, employee, Student

# Register your models here.

admin.site.register(employee)

admin.site.register(department)
admin.site.register(Student)
