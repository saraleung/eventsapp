from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length  = 250)
	datetime = models.DateTimeField()

class Performer(models.Model):
	name = models.CharField(max_length  = 50)
	event = models.ForeignKey(Event, default='', on_delete=models.CASCADE)



