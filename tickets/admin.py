from django.contrib import admin

from .models import Events, Prices, TicketsSold

# Register your models here.
admin.site.register(Events)
admin.site.register(Prices)
admin.site.register(TicketsSold)