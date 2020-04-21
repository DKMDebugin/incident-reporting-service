"""Viewset for the Definition model"""

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Definition
from api.serializers import DefinitionSerializer


class DefinitionViewset(viewsets.ModelViewSet):
    """Viewset for the Definition model"""
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

    @action(methods=['delete'], detail=False, url_path="bulk_delete")
    def bulk_destroy(self, request):
        def_ids = request.query_params.get('def_ids', None)
        def_ids = [int(id) for id in def_ids.split(",")]
        if def_ids is not None:
            return Definition.objects.bulk_delete(def_ids=def_ids)
        return Response(status=status.HTTP_404_NOT_FOUND)
