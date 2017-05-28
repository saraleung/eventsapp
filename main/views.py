from django.shortcuts import render
from eventsapp.models import Event, Performer
# Create your views here.
def home(request):
	events = Event.objects.all()
	performers = Performer.objects.all()
	return render(request, 'index.html', {'events' : events, 'performers' : performers})
