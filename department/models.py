from django.db import models
import django

import datetime

# Create your models here.
class Department(models.Model):
    dept_code = models.CharField(max_length=30)
    dept_name = models.CharField(max_length=30)

    def __str__(self):
       return "{{ code : '{}' , name : '{}'}}".format(self.dept_code,self.dept_name)
        #return self.dept_name


class Employee(models.Model):
    emp_fname = models.CharField(max_length=30)
    emp_lname = models.CharField(max_length=30)
    emp_phone = models.CharField(max_length=30)
    emp_created = models.DateTimeField(default=datetime.datetime.now())
    emp_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_fname

    def getAll(self):
        mylist = list()
        employee = Employee.objects.all()
        
        for obj in employee:
            value='{{"emp_fname":{},"emp_lname":{},"emp_phone":{},"emp_department":{} }}'.format(obj.emp_fname,obj.emp_lname,obj.emp_phone,obj.emp_department.id)
            mylist.append(value)
            
        return mylist
    
  
