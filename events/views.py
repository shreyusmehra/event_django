from django.shortcuts import redirect, render
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, response
from .models import Event, Venue
from.forms import VenueForm, EventForm
from django.http import HttpResponse
import string
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def venue_pdf(request): # Generate a PDF file of Venues
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add venues to text

    #Designate the model
    venues = Venue.objects.all()
    
    # Create blank list
    lines =[]

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.pin_code)
        lines.append(venue.phone)
        lines.append(venue.website)
        lines.append(venue.email)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    # Write of pdf file
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')


def venue_csv(request): # Generate a CSV file of All Venues
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = venue.csv'

    # Create CSV writer
    writer = csv.writer(response)

    #Designate the model
    venues = Venue.objects.all()

    # Add Column headings to the csv file
    writer.writerow(['Venue Name', 'Address', 'Pin Code','Phone', 'Website', 'Email ID'])
    
    #Loop thru and output
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.pin_code, venue.phone, venue.website, venue.email])
    
    return response


def venue_text(request): # Generate a text file containing all venues
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = venue.txt'
    
    #lines = ["This is line 1\n",
    #"This is line 2\n",
    #"This is line 3\n"]

    #Designate the model
    venues = Venue.objects.all()
    
    # Create blank list
    lines =[]
    #Loop thru and output
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.pin_code}\n{venue.phone}\n{venue.website}\n{venue.email}\n\n')
    
    # Write on text file
    response.writelines(lines)
    return response


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event )
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html',
    {"event" : event, "form" : form })

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)

        return render(request, 'events/search_venues.html',
        {"searched" : searched, "venues" : venues})

    else:
        return render(request, 'events/search_venues.html',
        {})


def add_event(request):
    submitted = False
    if request.method  == "POST":
        form = EventForm(request.POST)
        if form .is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'events/add_event.html', {"form" : form, 'submitted' : submitted,})
    

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue )
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'events/update_venue.html',
    {"venue" : venue, "form" : form })

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)

        return render(request, 'events/search_venues.html',
        {"searched" : searched, "venues" : venues})

    else:
        return render(request, 'events/search_venues.html',
        {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html',
    {"venue" : venue,})

def list_venues(request):
    venue_list = Venue.objects.all().order_by('name')# ? for random order
    return render(request, 'events/venue.html',
    {"venue_list" : venue_list,})


def add_venue(request):
    submitted = False
    if request.method  == "POST":
        form = VenueForm(request.POST)
        if form .is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'events/add_venue.html', {"form" : form, 'submitted' : submitted,})
    

def all_events(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'events/event_list.html',
    {"event_list" : event_list,})


def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):

    name = "Shreyus"
    month = month.capitalize()

    #Convert month from name to number
    month_number  = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    #get current year
    now = datetime.now()
    current_year = now.year
    # current time
    time = now.strftime('%I:%M:%S %p')
    #current date
    date = now.date
    return render(request, 'events/home.html',{"name" : name, "year" : year, "month" : month, 
    "month_number" : month_number, "cal" : cal, "current_year" : current_year, "time" : time, "date" : date})