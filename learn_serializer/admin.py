from django.contrib import admin

# Register your models here.
from .models import Department ,Employeee ,Project ,Employee_Project

admin.site.register(Department)
admin.site.register(Employeee)
admin.site.register(Project)
admin.site.register(Employee_Project)