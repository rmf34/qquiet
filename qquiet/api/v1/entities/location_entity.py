from rest_framework import viewsets

from .serializers import LocationSerializer
from .models import Location


class LocationEntity(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
