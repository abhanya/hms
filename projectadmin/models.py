from django.db import models

# Create your models here.

class Department(models.Model):
    departments = models.CharField(max_length=50)
    description = models.CharField(max_length=50,default='')

class HospitalAdmin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)