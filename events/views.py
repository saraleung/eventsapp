from django.shortcuts import render
from events.models import Event, Performer
# Create your views here.
def home(request):
	eventsAll = Event.objects.all()
	performers = Performer.objects.all()
	return render(request, 'index.html', {'events' : eventsAll, 'performers' : performers})
