from django.urls import path
from . import views

app_name = 'gezi'

urlpatterns = [
    path('', views.index, name='index'),
    path('trip/<int:trip_id>/', views.trip, name='trip'),
    path('person/<int:person_id>/', views.person, name='person'),
    path('traveler/<int:traveler_id>/', views.traveler, name='traveler'),
    path('addnewperson', views.addnewperson, name='addnewperson'),
    path('adding_result', views.adding_result, name='adding_result'),
    path('delete_person', views.delete_person, name='delete_person'),
    path('delete_person_result', views.delete_person_result, name='delete_person_result')

]