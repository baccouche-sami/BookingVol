from django.db import models

class Vol(models.Model):

      class Meta:
            verbose_name = "Vol"
            ordering = ['id', 'depart', 'arrive', 'montant']

      STATUTS = (
            ('CDG', ('CDG')),
            ('FJK', ('FJK')),
            ('DTW', ('DTW'))
      )

      depart = models.CharField(max_length=255, null = False, choices=STATUTS)
      arrive = models.CharField(max_length=255, null = False, choices=STATUTS)
      montant = models.IntegerField()
      places = models.IntegerField()

      
      def __str__(self):
            return self.depart + " -> " + self.arrive
    