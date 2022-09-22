from . import viewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'vols', viewsets.VolViewSet)
router.register(r'reservations', viewsets.ReservationViewSet)