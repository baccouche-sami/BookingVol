from django.db import models

class Vol(models.Model):

      class Meta:
            verbose_name = "Vol"
            ordering = ['id', 'depart', 'arrive', 'montant']

      AEROPORTS = (
            ('CDG', ('CDG')),
            ('FJK', ('FJK')),
            ('LAD', ('LAD')),
            ('DTW', ('DTW'))
      )

      code = models.CharField(max_length=255, null = True)
      depart = models.CharField(max_length=255, null = False, choices=AEROPORTS)
      arrive = models.CharField(max_length=255, null = False, choices=AEROPORTS)
      montant = models.IntegerField()
      places = models.IntegerField()

      
      def __str__(self):
            return self.depart + " -> " + self.arrive
    