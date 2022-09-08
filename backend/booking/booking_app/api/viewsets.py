from rest_framework.viewsets import ModelViewSet
from .serializers import VolSerializer, ReservationSerializer, UserSerializer
from .filters import UserFilter

from django.contrib.auth.models import User
from ..models.vol import Vol
from ..models.reservation import Reservation

from .utils import custom_query
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

