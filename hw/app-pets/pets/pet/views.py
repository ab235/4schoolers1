from django.shortcuts import render
from .models import Pet
# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hi there!")

def add(request, name, type):
    newbie = Pet(name=name, type=type)
    newbie.save()
    return HttpResponse('Pet: {} was logged'.format(name))

def delete(request, name):
    bye = Pet.objects.get(name=name)
    bye.delete()
    return HttpResponse('Pet was taken out of system')

def all(request):
    everypet = {}
    pets = Pet.objects.all()
    everypet['pets'] = list(pets)
    return render(request, 'pets.jinja', everypet)

def some(request, name):
    context = {}
    pets = Pet.objects.filter(name=name)
    context['pets'] = list(pets)
    return render(request, 'pets.jinja', context)
