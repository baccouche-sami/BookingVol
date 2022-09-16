from rest_framework import serializers
from ..models.vol import Vol
from ..models.reservation import Reservation
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'last_name', 'first_name', 'email', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}


class VolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vol
        fields = ('id', 'code', 'url', 'depart', 'arrive', 'montant', 'places')


class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ('id', 'nom', 'prenom', 'nb_place', 'url', 'vol', 'montant', 'retour_inclut', 'champagne', 'first_class', 'currency', 'date_depart', 'date_retour')
        extra_kwargs = {'montant': {'read_only': True}}
