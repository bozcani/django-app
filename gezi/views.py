from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, welcome to the Gezi App. Share your trip experience!")

def trip(request, trip_id):
    return HttpResponse("You're looking at trip %s." % trip_id)    

def person(request, person_id):
    return HttpResponse("You're looking at person %s." % person_id)    

def traveler(request, traveler_id):
    return HttpResponse("You're looking at traveler %s." % traveler_id)    
