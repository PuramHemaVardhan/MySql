from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sprinciple=models.CharField(max_length=100)
class student(models.Model):
    stname=models.CharField(max_length=100)
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    