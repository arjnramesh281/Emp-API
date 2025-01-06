from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    address=models.TextField()
    position=models.CharField(max_length=50)
    salary=models.IntegerField()
    experiance=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()