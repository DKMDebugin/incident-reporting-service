"""Viewset for the Type model"""

from rest_framework import viewsets

from api.models import Type
from api.serializers import TypeSerializer


class TypeViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset for the Type model"""
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
