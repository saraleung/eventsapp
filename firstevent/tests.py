from django.test import TestCase
from firstevent.models import Event, Performer

class TestEvent(TestCase):
	def setUp(self):
		Event.objects.create(name="Starboy", datetime='2017-05-29 13:00:00')

	def test_event_created(self):
		newEvent = Event.objects.get(name="Starboy")
		#self.assertEqual(newEvent.datetime.strftime("%Y-%m-%d"), '2017-05-29')
		self.assertEqual(newEvent.name, 'Starboy')

class TestPerformer(TestCase):
	def setUp(self):
		Event.objects.create(name="Starboy", datetime='2017-05-29 13:00:00')
		testEvent = Event.objects.get(name="Starboy")
		Performer.objects.create(name="Weeknd", event=testEvent)

	def test_performer_added(self):
		newPerformer = Performer.objects.get(name="Weeknd")
		self.assertEqual(newPerformer.name, 'Weeknd')

