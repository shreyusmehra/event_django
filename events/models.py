from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):#Venue table
    name = models.CharField('Venue Name', max_length = 120)
    address = models.CharField(max_length = 300)
    pin_code = models.CharField('Pin Code',max_length = 6)
    phone = models.CharField('Contact Phone', max_length = 10, blank=True)
    website = models.URLField('Website', blank = True)
    email = models.EmailField('Email', blank = True)

    def __str__(self):
        return self.name

class Website_user(models.Model):#Website user table
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):#Event table
    name = models.CharField('Event Name', max_length = 120,)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, blank = True, null = True, on_delete = models.CASCADE)
    #venue = models.CharField(max_length = 120)
    manager = models.ForeignKey(User, blank = True, null = True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Website_user, blank = True)

    def __str__(self):
        return self.name