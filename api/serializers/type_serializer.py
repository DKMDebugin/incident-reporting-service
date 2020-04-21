"""Serializer for the Type model"""

from rest_framework import serializers

from api.models import Type


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Type model"""

    class Meta:
        model = Type
        fields = ("url", "id", "name", "created_at", "updated_at")
