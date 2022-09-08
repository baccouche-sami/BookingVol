from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .vol import Vol

class Reservation(models.Model):

  class Meta:
        verbose_name = "Reservation"
        ordering = ['id', 'vol', 'user', 'date']

  vol = models.ForeignKey(Vol, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  date = models.DateTimeField(default=timezone.now)

  
  def __str__(self):
      return self.user.first_name + " " + self.user.last_name + "(" + self.vol.__str__ + ")"
    