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
    trip = get_object_or_404(Trip, pk=trip_id)
    travel_list = Traveler.objects.filter(trip=trip)
    context = {
        'trip':trip,
        'travel_list':travel_list
    }
    return render(request, 'gezi/trip.html', context)


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

def add_person(request):
    return render(request, 'gezi/add_person.html')

def add_person_result(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    birthdate = request.GET.get('birthdate')

    new_person = Person(first_name=first_name, last_name=last_name, birthdate=birthdate)
    new_person.save()
    context = {
        'first_name':first_name,
        'last_name':last_name,
        'birthdate':birthdate
    }    
    return render(request, 'gezi/add_person_result.html',context)


def delete_person(request):
    person_list = Person.objects.all()
    context = {
        'person_list':person_list
    }
    return render(request, 'gezi/delete_person.html', context)

def delete_person_result(request):
    person_id = request.GET.get('person_id')
    person = Person.objects.get(pk=person_id)
    context = {
        'first_name':person.first_name,
        'last_name':person.last_name
    }
    person.delete()

    return render(request, 'gezi/delete_person_result.html', context)

def add_traveler(request):
    person_list = Person.objects.all()
    trip_list = Trip.objects.all()

    context = {
        'person_list':person_list,
        'trip_list':trip_list
    }
    return render(request, 'gezi/add_traveler.html', context)

def add_traveler_result(request):
    person_id = request.GET.get('person_id')
    trip_id = request.GET.get('trip_id')
    person = Person.objects.get(pk=person_id)
    trip = Trip.objects.get(pk=trip_id)

    new_traveler = Traveler(trip=trip, person=person)
    new_traveler.save()
    context = {
        'first_name':person.first_name,
        'last_name':person.last_name,
        'trip_name':trip.trip_name,
        'city':trip.city,
        'date':trip.date
    }

    return render(request, 'gezi/add_traveler_result.html', context)

def delete_traveler(request):
    traveler_list = Traveler.objects.all()
    context = {
        'traveler_list':traveler_list
    }
    return render(request, 'gezi/delete_traveler.html', context)

def delete_traveler_result(request):
    traveler_id = request.GET.get('traveler_id')
    traveler = Traveler.objects.get(pk=traveler_id)
    context = {
        'first_name':traveler.person.first_name,
        'last_name':traveler.person.last_name,
        'trip_name':traveler.trip.trip_name
    }
    traveler.delete()

    return render(request, 'gezi/delete_traveler_result.html', context)   