from django.shortcuts import render, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Person, Trip, Traveler
# Create your views here.
def index(request):
    trips = Trip.objects.all()
    persons = Person.objects.all()
    travelers = Traveler.objects.all()


    template = loader.get_template('gezi/index.html')
    context = {
        'person_list':persons,
        'trip_list':trips,
        'traveler_list':travelers

    }

    return HttpResponse(template.render(context, request))

def trip(request, trip_id):
    return HttpResponse("You're looking at trip %s." % trip_id)    

def person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    travel_list = Traveler.objects.filter(person=person)
    context = {
        'person':person,
        'travel_list':travel_list
    }
    return render(request, 'gezi/person.html', context)

def traveler(request, traveler_id):
    return HttpResponse("You're looking at traveler %s." % traveler_id)    
