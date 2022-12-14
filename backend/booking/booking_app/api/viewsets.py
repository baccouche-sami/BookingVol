import math

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import VolSerializer, ReservationSerializer, UserSerializer, TrainSerializer
from .filters import UserFilter

from django.contrib.auth.models import User
from django.http import QueryDict
from ..models.vol import Vol
from ..models.train import Train
from ..models.reservation import Reservation
from .utils import custom_query, str_to_bool, get_currency


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

            self.queryset = self.queryset.filter(custom_query(self.request.query_params.dict()))
            
            return self.queryset

class TrainViewSet(ModelViewSet):
    queryset = Train.objects.order_by('pk')
    serializer_class = TrainSerializer
    executed = False
    
    def get_queryset(self):
        if not self.executed :
            self.executed = True

            self.queryset = self.queryset.filter(custom_query(self.request.query_params.dict()))
            
            return self.queryset


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.order_by('pk')
    serializer_class = ReservationSerializer
    executed = False
    
    def get_queryset(self):
        if not self.executed :
            self.executed = True
            
            return self.queryset.filter(custom_query(self.request.query_params.dict()))

    def create(self, request):

        content_type = request.data.get('transport')

        transport = Vol.objects.get(pk=int(request.data.get('transport'))) if content_type == "8" else Train.objects.get(pk=int(request.data.get('transport')))

        reservations = Reservation.objects.filter(transport = int(request.data.get('transport')))

        if transport.places <= len(reservations) : return Response("No more seat available", status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
        champagne = str_to_bool(request.data.get('champagne'))
        retour_inclut = str_to_bool(request.data.get('retour_inclut'))
        first_class = str_to_bool(request.data.get('first_class'))

        montant_vol = transport.montant * int(request.data.get('nb_place'))

        if champagne : montant_vol += 100

        

        if first_class : 

            first_class_nb = math.ceil(transport.places * 0.1)

            reservations_first_class = Reservation.objects.filter(transport = int(request.data.get('transport')), first_class = True)

            if first_class_nb <= len(reservations_first_class) : return Response("No more first class seat available", status=status.HTTP_406_NOT_ACCEPTABLE)

            if content_type == "8" : 
                montant_vol += montant_vol * 1.5
            else :
                montant_vol += 50

        if retour_inclut : montant_vol *= 1.95

        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid() : serializer.save(montant=montant_vol, transport = int(request.data.get('transport')), champagne = champagne, retour_inclut = retour_inclut)

        return Response(request.data, status=status.HTTP_201_CREATED)
        
