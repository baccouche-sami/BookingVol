from django.db import models

class Train(models.Model):

      class Meta:
            verbose_name = "Train"
            ordering = ['id', 'nom',  'depart', 'arrive', 'montant']

      GARES = (
            ('CDG', ('CDG')),
            ('JFK', ('JFK')),
            ('EWR', ('EWR')),
            ('ORD', ('ORD'))
      )

      code = models.CharField(max_length=255, null = True)
      nom = models.CharField(max_length=255, null = True)
      depart = models.CharField(max_length=255, null = False, choices=GARES)
      arrive = models.CharField(max_length=255, null = False, choices=GARES)
      montant = models.IntegerField()
      places = models.IntegerField()

      
      def __str__(self):
            return self.depart + " -> " + self.arrive
    