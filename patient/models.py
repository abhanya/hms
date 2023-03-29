from django.db import models
from common.models import Patient,Doctor
from projectadmin.models import Department

# Create your models here.

class Booking(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=True)
    symptoms = models.CharField(max_length=500,default='')
    cunsultion_type = models.ForeignKey(Department,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
