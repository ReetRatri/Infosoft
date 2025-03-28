from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author =  models.CharField(max_length=200)
    published_date = models.DateField()
    author_dob = models.DateField()
    

class Author(models.Model):
    author =  models.CharField(max_length=200)
    number_of_books = models.IntegerField()




class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length =200)

    def __str__(self):
        return self.department_name

class Employeee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    department_id = models.ForeignKey(Department ,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.project_name

class Employee_Project(models.Model):
    employee_id = models.ForeignKey(Employeee, on_delete=models.CASCADE)
    project_name = models.ForeignKey(Project , on_delete=models.CASCADE )
    hours_worked = models.IntegerField()

    def __str__(self):
        return f"{self.employee_id.name} - {self.project_name.project_name}"



