from django.urls import path, include
from . import views, core_views

app_name = 'gezi'

urlpatterns = [
    path('', views.index, name='index'),
    path('trip/<int:trip_id>/', views.trip, name='trip'),
    path('person/<int:person_id>/', views.person, name='person'),
    path('traveler/<int:traveler_id>/', views.traveler, name='traveler'),
    path('add_person', views.add_person, name='add_person'),
    path('add_person_result', views.add_person_result, name='add_person_result'),
    path('delete_person', views.delete_person, name='delete_person'),
    path('delete_person_result', views.delete_person_result, name='delete_person_result'),
    path('add_traveler', views.add_traveler, name='add_traveler'),
    path('add_traveler_result', views.add_traveler_result, name='add_traveler_result'),
    path('delete_traveler', views.delete_traveler, name='delete_traveler'),
    path('delete_traveler_result', views.delete_traveler_result, name='delete_traveler_result'),
    path('add_trip', views.add_trip, name='add_trip'),
    path('add_trip_result', views.add_trip_result, name='add_trip_result'),
    path('delete_trip', views.delete_trip, name='delete_trip'),
    path('delete_trip_result', views.delete_trip_result, name='delete_trip_result'),

    path('u/<str:username>/', views.user_profile, name='user_profile'),

    path('accounts/', include('django.contrib.auth.urls')),

    # Core views
    path('signup/', core_views.signup, name='signup'),


]