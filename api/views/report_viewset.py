"""Viewset for the Report model"""

from rest_framework import viewsets

from api.models import Report
from api.serializers import ReportSerializer


class ReportViewset(viewsets.ModelViewSet):
    """Viewset for the Report model"""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
