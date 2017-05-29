from django.shortcuts import render
from firstevent.models import Event, Performer

def home(request):
	events = Event.objects.all()
	performers = Performer.objects.all()
	return render(request, 'index.html', {'events' : events, 'performers' : performers})
