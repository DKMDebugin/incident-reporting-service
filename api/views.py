from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

import py_eureka_client.eureka_client as eureka_client

from .models import Frequency, Type, Definition, Report
from .serializers import (
                           FrequencySerializer, TypeSerializer,
                           DefinitionSerializer, ReportSerializer
                        )
from .permissions import IsReadOnly


class FrequencyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer

class TypeViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class DefinitionViewset(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

    @action(methods=['delete'], detail=False, url_path="bulk_delete")
    def bulk_destroy(self, request):
        def_ids= request.query_params.get('def_ids', None)
        def_ids = [int(id) for id in def_ids.split(",")]
        if def_ids is not None:
            return Definition.objects.bulk_delete(def_ids=def_ids)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ReportViewset(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
