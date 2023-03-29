from django.db import models
from common.models import Patient,Doctor
from patient.models import Booking
# Create your models here.

class Description(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,default="")
    Booking = models.ForeignKey(Booking,on_delete=models.CASCADE,default="")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    discription_date = models.DateField(auto_now=True)
