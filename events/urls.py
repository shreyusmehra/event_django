from django.urls import path
from . import views

urlpatterns = [
    #path converters
    # int:numbers
    #str:strings
    #path:whole urls / 
    #slug:hyphen and underscores
    #UUID: Universally unique indentifiers

    path('',views.home, name="home"),
    path('<int:year>/<str:month>/',views.home, name="home"),
    path('events', views.all_events, name = "list-events"),
    path('add_venue', views.add_venue, name='add-venue'),
]