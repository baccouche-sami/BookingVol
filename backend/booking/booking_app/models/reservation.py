from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .vol import Vol

class Reservation(models.Model):

      class Meta:
            verbose_name = "Reservation"
            ordering = ['id', 'nom', 'prenom', 'nb_place', 'transport', 'montant', 'champagne', 'first_class', 'currency', 'date_depart', 'date_retour']
      
      CURRENCY = (
            ('EURO', ('EURO')),
            ('DOLLAR', ('DOLLAR'))
      )

      nom = models.CharField(max_length=255, null = False)
      prenom = models.CharField(max_length=255, null = False)
      
      retour_inclut = models.BooleanField(default=False)
      champagne = models.BooleanField(default=False)
      first_class = models.BooleanField(default=False)
      nb_place = models.IntegerField(default=1)
      montant = models.IntegerField()
      currency = models.CharField(max_length=6, choices=CURRENCY)
      date_depart = models.DateTimeField(null=True)
      date_retour = models.DateTimeField(null=True)

      content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
      transport = models.PositiveIntegerField()
      content_object = GenericForeignKey('content_type', 'transport')

  
      def __str__(self):
            return self.user.first_name + " " + self.user.last_name + "(" + self.vol.__str__ + ")"
    