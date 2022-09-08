from django.db import models

class Vol(models.Model):

  class Meta:
        verbose_name = "Vol"
        ordering = ['id', 'depart', 'arrive', 'montant']

  depart = models.CharField(max_length=255, null = False)
  arrive = models.CharField(max_length=255, null = False)
  montant = models.IntegerField()
  places = models.IntegerField()

  
  def __str__(self):
      return self.depart + " -> " + self.arrive
    