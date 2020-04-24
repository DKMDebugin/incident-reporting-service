"""Serializer for the Job model"""

from rest_framework import serializers

from job_scheduler.models import Job, Interval, Type


# class IntervalSerializer(serializers.ModelSerializer):
#     """Serializer for the Job model"""
#
#     class Meta:
#         model = Interval
#         fields = ('interval')
#
#
# class TypeSerializer(serializers.ModelSerializer):
#     """Serializer for the Job model"""
#
#     class Meta:
#         model = Type
#         fields = ('name')


class JobSerializer(serializers.ModelSerializer):
    """Serializer for the Job model"""
    # interval = IntervalSerializer()
    # job_type = TypeSerializer()

    class Meta:
        model = Job
        fields = ('id', 'name', 'job_type', 'interval', 'status',
                  'execute_at', 'executed', 'created_at', 'updated_at')
        depth = 1
