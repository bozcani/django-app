from django.db import models

# Create your models here.
class Trip(models.Model):
    trip_name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    date = models.DateTimeField('date of the trip')

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)    
    birthdate = models.IntegerField()    

class Traveler(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
