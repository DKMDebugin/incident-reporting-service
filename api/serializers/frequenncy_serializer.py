"""Serializer for the Frequency model"""

from rest_framework import serializers

from api.models import Frequency


class FrequencySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Frequency model"""

    class Meta:
        model = Frequency
        fields = ("url", "id", "name", "created_at", "updated_at")
