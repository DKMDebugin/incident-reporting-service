from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.response import Response

from .models import Frequency, Type, Definition, Report
from .serializers import (
                           FrequencySerializer, TypeSerializer,
                           DefinitionSerializer, ReportSerializer
                        )


class FrequencyViewset(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer

class TypeViewset(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class DefinitionViewset(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

    def bulk_delete(self, request, def_list=[]):
        return Definition.objects.bulk_delete(def_list=def_list)

class ReportViewset(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
