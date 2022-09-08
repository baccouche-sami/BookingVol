import site
from django.contrib import admin
from .models.vol import Vol
from .models.reservation import Reservation

admin.site.register(Vol)
admin.site.register(Reservation)