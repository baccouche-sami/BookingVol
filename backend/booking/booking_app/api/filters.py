from .serializers import *
from django_filters import CharFilter, FilterSet
from django.contrib.auth.models import User
from ..models.vol import Vol
from ..models.reservation import Reservation


class UserFilter(FilterSet):
    username = CharFilter(lookup_expr='icontains')
    last_name = CharFilter(lookup_expr='icontains')
    first_name = CharFilter(lookup_expr='icontains')
    email = CharFilter(lookup_expr='icontains')
    
    class Meta:
        model= User
        fields = ['id','username', 'last_name', 'first_name', 'email']

class VolFilter(FilterSet):
    
    class Meta:
        model= Vol
        fields = ['id', 'code', 'depart', 'arrive', 'montant', 'places']

class ReservationFilter(FilterSet):
    
    class Meta:
        model= Reservation
        fields = ['id', 'nom', 'prenom', 'nb_place', 'vol', 'montant', 'retour_inclut', 'champagne', 'first_class', 'currency', 'date_depart', 'date_retour']

