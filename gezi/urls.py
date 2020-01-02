from django.urls import path
from . import views

app_name = 'gezi'

urlpatterns = [
    path('', views.index, name='index'),
    path('trip/<int:trip_id>/', views.trip, name='trip'),
    path('person/<int:person_id>/', views.person, name='person'),
    path('traveler/<int:traveler_id>/', views.traveler, name='traveler')

]