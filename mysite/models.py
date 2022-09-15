from django.db import models

class Person(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)  
    file = models.FileField(blank=True) # for creating file input  