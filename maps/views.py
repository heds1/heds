from django.shortcuts import render
from config.settings import MAPBOX_TOKEN
from maps.models import Location

def index(request):
    location = Location.objects.get(id=1)
    location_json = location.serialize()
    context = {
        'MAPBOX_TOKEN': MAPBOX_TOKEN,
        'location': location_json,
    }
    return render(request, 'index.html', context)
