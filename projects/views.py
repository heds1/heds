from django.shortcuts import render
from config.settings import MAPBOX_TOKEN
from projects.models import Location

def index(request):
    return render(request, 'index.html')
    

def map(request):
    location = Location.objects.get(id=1)
    location_json = location.serialize()
    context = {
        'MAPBOX_TOKEN': MAPBOX_TOKEN,
        'location': location_json,
    }
    return render(request, 'map.html', context)



