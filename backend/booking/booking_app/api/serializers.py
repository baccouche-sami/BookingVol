from rest_framework import serializers
from ..models.vol import Vol
from ..models.train import Train
from ..models.reservation import Reservation
from django.contrib.auth.models import User
from .utils import get_currency


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'last_name', 'first_name', 'email', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}


class VolSerializer(serializers.ModelSerializer):

    price_map = serializers.SerializerMethodField()

    class Meta:
        model = Vol
        fields = ('id', 'code', 'url', 'depart', 'arrive', 'montant', 'places', 'price_map')

    def get_price_map(self, obj):
        currencies = get_currency()
            
        montant = obj.montant

        price_dict = {

        }

        for currency in currencies:
            price_dict[currency] = montant * float(currencies[currency])
        
        return price_dict

class TrainSerializer(serializers.ModelSerializer):

    price_map = serializers.SerializerMethodField()

    class Meta:
        model = Train
        fields = ('id', 'code', 'url', 'depart', 'arrive', 'montant', 'places', 'price_map')

    def get_price_map(self, obj):
        currencies = get_currency()
            
        montant = obj.montant

        price_dict = {

        }

        for currency in currencies:
            price_dict[currency] = montant * float(currencies[currency])
        
        return price_dict

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ('id', 'nom', 'prenom', 'nb_place', 'url', 'content_type', 'transport', 'montant', 'retour_inclut', 'champagne', 'first_class', 'currency', 'date_depart', 'date_retour')
        extra_kwargs = {'montant': {'read_only': True}}
