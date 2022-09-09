from wsgiref.util import request_uri
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import VolSerializer, ReservationSerializer, UserSerializer
from .filters import UserFilter

from django.contrib.auth.models import User
from ..models.vol import Vol
from ..models.reservation import Reservation



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

            return self.queryset.filter(custom_query(self.request.query_params.dict()))

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.order_by('pk')
    serializer_class = ReservationSerializer
    executed = False
    
    def get_queryset(self):
        if not self.executed :
            self.executed = True

            return self.queryset.filter(custom_query(self.request.query_params.dict()))

    def create(self, request):
        request.data._mutable=True

        request.data["champagne"] = str_to_bool(request.data.get('champagne'))
        request.data["retour_inclut"] = str_to_bool(request.data.get('retour_inclut'))

        montant_vol = Reservation.objects.get(pk=request.data.get('vol')).montant * request.data.get('nb_place')
        print(montant_vol)
        if request.data.get('champagne') : montant_vol += 100
        print(montant_vol)
        if request.data.get('retour_inclut') : montant_vol *= 1.95

        print(montant_vol)
        request.data["montant"] = montant_vol
        request.data.pop('csrfmiddlewaretoken')
        request.data["vol_id"] = int(request.data.pop('vol')[0])
        request.data["user_id"] = int(request.data.pop('user')[0])

        Reservation(**request.data.dict()).save()

        return Response(request.data, status=status.HTTP_201_CREATED)
        
