from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Events(models.Model):
    eventTitle = models.CharField(max_length=50)
    eventDescription = models.TextField()
    eventDate = models.DateField()
    eventPoster = models.ImageField(upload_to = "posters/%Y/%m/%d/")
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.eventTitle

class Prices(models.Model):
    forEvent = models.ManyToManyField(to=Events)
    eventPrice = models.IntegerField(default=0)
    
    def __str__(self):
        return "Event_ID: {}, Event Price: {}".format(self.forEvent, self.eventPrice)

class TicketsSold(models.Model):
    event = models.ManyToManyField(to=Events)
    price = models.ManyToManyField(to=Prices)
    holdersName = models.CharField(max_length=30)
    holdersEmail = models.EmailField()
    holdersPhoneNumber = models.IntegerField()
    ticketVerificationCode = models.CharField(max_length=50)
    # ticketQRCode = models.ImageField(upload_to = "verification/%Y/%m/%d/") - not needed. QR will be generated automatically 
    
    def __str__(self):
        return "Holders Name: {}, Event: {}, Price: {}".format(self.holdersName, self.event, self.price)
