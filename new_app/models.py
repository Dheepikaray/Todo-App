
from django.db import models
class Todo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    date = models.DateField()

#add date field

# class AppointmentSchedule(models.Model):
#     date=models.DateField

# Create your models here.
