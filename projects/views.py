from django.shortcuts import render
from config.settings import MAPBOX_TOKEN
from projects.models import Location

def index(request):
    return render(request, 'index.html')
    

def map(request):
    # location = Location.objects.get(id=1)
    # location_json = location.serialize()

    # update - allow for multiple sites. we'll be doing json.dumps here.
    from json import dumps
    locations = Location.objects.all()
    location_list = [l.serialize() for l in locations]
    location_dict = {"type": "FeatureCollection",
        "features": location_list}
    location_json = dumps(location_dict)

    context = {
        'MAPBOX_TOKEN': MAPBOX_TOKEN,
        'locations': location_json,
    }
    return render(request, 'map.html', context)



