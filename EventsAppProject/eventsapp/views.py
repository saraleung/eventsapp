from django.shortcuts import render
from eventsapp.models import Event
# Create your views here.
def home(request):
	return render(request, 'index.html')
