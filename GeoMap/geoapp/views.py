from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer

class PlaceDetailAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer