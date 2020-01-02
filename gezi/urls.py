from django.urls import path
from . import views

app_name = 'gezi'

urlpatterns = [
    path('', views.index, name='index')
]