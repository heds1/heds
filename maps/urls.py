from django.urls import path
from maps import views

urlpatterns = [
    path(route='', view=views.index, name='index')
]