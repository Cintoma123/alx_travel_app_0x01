from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from .models import Listing, Booking , User
from rest_framework import viewsets, status
from .serializers import ListingSerializer , BookingSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

router = DefaultRouter()
router.register(r'listing', ListingViewSet)
router.register(r'user', UserViewSet)
router.register(r'booking',BookingViewSet)

urlpatterns = [
    path('retrieve_bookings_made_by_user/', UserViewSet.retrieve_bookings_made_by_user, name='retrieve_bookings_made_by_user'),
    path('list_made_by_user/', UserViewSet.list_made_by_user, name = 'list_made_by_user')
    path('delete_bookings_made_by_user/', UserViewSet.delete_bookings_made_by_user, name = 'delete_bookings_made_by_user')
    path('updated_bookings_made_by_user/'UserViewSet.updated_bookings_made_by_user, name = 'updated_bookings_made_by_user')
    path('', include(router.urls)),
]