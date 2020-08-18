from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('main', views.event, name='event'),
    path('services', views.community, name='services'),
    path('team', views.team, name='team'),
    path('camp', views.camp, name='bootcamps'),
    path('about', views.about, name='about'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('incubate', views.incubate, name='incubate'),
    path('it4gh', views.it4gh, name='it4gh'),
    path('ccoc', views.ccoc, name='ccoc'),
    # path('cont', views.contact, name='cont'),
    path('contact', views.contact, name='contact'),
]
