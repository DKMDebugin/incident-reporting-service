"""Serializer for the Report model"""

from rest_framework import serializers

from api.models import Report


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Report model"""

    class Meta:
        model = Report
        fields = ("url", "id", "definition", "status", "attachment",
                  "created_at", "updated_at")
