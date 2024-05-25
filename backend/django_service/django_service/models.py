from django.db import models

class Student(models.model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    middle_name = models.CharField(max_length=50)
    course = models.IntegerField(max_length=2)
    group = CharField(max_length=10)
    access_level = 2
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    access_level = 1