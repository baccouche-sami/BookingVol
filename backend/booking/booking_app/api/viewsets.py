import math
from wsgiref.util import request_uri
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import VolSerializer, ReservationSerializer, UserSerializer
from .filters import UserFilter

from django.contrib.auth.models import User
from django.http import QueryDict
from ..models.vol import Vol
from ..models.reservation import Reservation

import requests
import json



from .utils import custom_query, str_to_bool
class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer
    filterset_class = UserFilter

class VolViewSet(ModelViewSet):
    queryset = Vol.objects.order_by('pk')
    serializer_class = VolSerializer
    executed = False
    
    def get_queryset(self):
        if not self.executed :
            self.executed = True

            result = requests.get('https://api-6yfe7nq4sq-uc.a.run.app/flights')
            vols = []
            for external_vol in json.loads(result.content.decode('utf-8')):
                vol = Vol(code = external_vol["code"], depart = external_vol["departure"], arrive = external_vol["arrival"], montant = external_vol["base_price"], places = external_vol["plane"]["total_seats"])
                
                vols.append(vol)

            vols.extend(self.queryset.filter(custom_query(self.request.query_params.dict())))
            return vols

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.order_by('pk')
    serializer_class = ReservationSerializer
    executed = False
    
    def get_queryset(self):
        if not self.executed :
            self.executed = True
            
            return self.queryset.filter(custom_query(self.request.query_params.dict()))

    def create(self, request):

        vol = Vol.objects.get(pk=request.data.get('vol'))

        reservations = Reservation.objects.filter(vol = request.data.get('vol'))

        if vol.places <= len(reservations) : return Response("No more seat available", status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
        champagne = str_to_bool(request.data.get('champagne'))
        retour_inclut = str_to_bool(request.data.get('retour_inclut'))
        first_class = str_to_bool(request.data.get('first_class'))

        montant_vol = vol.montant * int(request.data.get('nb_place'))

        if champagne : montant_vol += 100

        

        if first_class : 

            first_class_nb = math.ceil(vol.places * 0.1)

            reservations_first_class = Reservation.objects.filter(vol = request.data.get('vol'), first_class = True)

            if first_class_nb <= len(reservations_first_class) : return Response("No more first class seat available", status=status.HTTP_406_NOT_ACCEPTABLE)

            montant_vol *= 1.5

        if retour_inclut : montant_vol *= 1.95

        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid() : serializer.save(montant=montant_vol, vol_id = int(request.data.get('vol')), champagne = champagne, retour_inclut = retour_inclut)

        return Response(request.data, status=status.HTTP_201_CREATED)
        

