from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .vol import Vol

class Reservation(models.Model):

      class Meta:
            verbose_name = "Reservation"
            ordering = ['id', 'nom', 'prenom', 'nb_place', 'vol', 'montant', 'champagne', 'first_class', 'date_depart', 'date_retour']
      
      nom = models.CharField(max_length=255, null = False)
      prenom = models.CharField(max_length=255, null = False)
      vol = models.ForeignKey(Vol, on_delete = models.CASCADE)
      retour_inclut = models.BooleanField(default=False)
      champagne = models.BooleanField(default=False)
      first_class = models.BooleanField(default=False)
      nb_place = models.IntegerField(default=1)
      montant = models.IntegerField()
      date_depart = models.DateTimeField(null=True)
      date_retour = models.DateTimeField(null=True)

  
      def __str__(self):
            return self.user.first_name + " " + self.user.last_name + "(" + self.vol.__str__ + ")"
    