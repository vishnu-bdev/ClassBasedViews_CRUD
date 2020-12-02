from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name    = models.CharField(max_length=100)    
    emp_id      = models.IntegerField(primary_key=True)
    email       = models.EmailField(max_length=100)
    salary      = models.IntegerField()

    class Meta:
        db_table = 'employee'