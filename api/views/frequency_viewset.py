"""Viewset for the Frequency model"""

from rest_framework import viewsets

from api.models import Frequency
from api.serializers import FrequencySerializer


class FrequencyViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset for the Frequency model"""
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer
