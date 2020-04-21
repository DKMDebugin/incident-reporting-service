"""Serializer for the Definition model"""

from rest_framework import serializers

from api.models import Definition


class DefinitionSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Definition model"""

    class Meta:
        model = Definition
        fields = ("url", "id", "frequency", "type", "project_uuid",
                  "roles", "users", "created_at", "updated_at",
                  "next_execution_date")
