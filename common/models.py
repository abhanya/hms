from django.db import models
from projectadmin.models import Department



# Create your models here.
class Patient(models.Model):
    pat_name = models.CharField(max_length=20)
    pat_email = models.CharField(max_length=60)
    pat_address = models.CharField(max_length=50)
    pat_gender = models.CharField(max_length=50)
    pat_phone = models.BigIntegerField()
    pat_pass = models.CharField(max_length=8) 
    age = models.IntegerField(default=False)

class Doctor(models.Model):
    doc_name = models.CharField(max_length=20)
    doc_email = models.CharField(max_length=60)
    doc_address = models.CharField(max_length=50)
    doc_gender = models.CharField(max_length=50)
    doc_phone = models.BigIntegerField()
    doc_pass = models.CharField(max_length=8) 
    doc_dob = models.DateField(auto_now=True)
    doc_username = models.CharField(max_length=50)
    doc_state = models.CharField(max_length=100)
    approve = models.BooleanField(default=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default="")

