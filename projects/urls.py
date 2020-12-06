from django.urls import path
from projects import views

urlpatterns = [
    path(route='', view=views.index, name='project-index'),
    path(route='map/', view=views.map, name='map'),
]