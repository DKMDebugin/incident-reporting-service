from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import (Frequency, Type,
                    Definition, Report)

class FrequencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frequency
        fields = ("url", "id", "name", "created_at", "updated_at")

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ("url", "id", "name", "created_at", "updated_at")

class DefinitionSerializer(WritableNestedModelSerializer):
    frequency = FrequencySerializer()
    type = TypeSerializer()
    class Meta:
        model = Definition
        fields = ("url", "id", "frequency", "type", "project_uuid",
                    "roles", "users", "created_at", "updated_at",
                    "next_execution_date")

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ("url", "id", "definition", "status", "attachment",
                    "created_at", "updated_at")
