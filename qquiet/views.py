# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the qquiet index.")


from rest_framework import viewsets#, views

from .serializers import LocationSerializer
from .models import Location


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer

