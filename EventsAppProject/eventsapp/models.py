from django.db import models

# Create your models here.

class Performer(models.Model):
	name = models.CharField(max_length  = 50)

class Event(models.Model):
	name = models.CharField(max_length  = 250)
	datetime = models.DateTimeField()
	performer= models.ForeignKey(Performer, on_delete=models.CASCADE)

