from django.http import HttpResponse
from django.shortcuts import render

from base.models import Room

def home(request):
    queryset = Room.objects.all()
    context = {'rooms': queryset}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)