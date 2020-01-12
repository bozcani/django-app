from django.shortcuts import render, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Person, Trip, Traveler

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('gezi/')
    else:
        form = UserCreationForm()
    return render(request, 'gezi/signup.html', {'form': form})
