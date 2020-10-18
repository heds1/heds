from django.urls import path
from blog import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='posts', view=views.posts, name='posts'),
    path(route='posts/<slug:slug>/', view=views.detail, name='detail'),
    path(route='tags/<tag>/', view=views.tag, name='tag'),
    path(route='contact/', view=views.contact, name='contact'),
    path(route='privacy/', view=views.privacy, name='privacy'),
    path(route='thanks/', view=views.thanks, name='thanks'),
    path(route='comment/', view=views.comment, name='comment'),
]