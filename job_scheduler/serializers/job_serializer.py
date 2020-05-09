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
    # url = serializers.SerializerMethodField()
    #
    # def get_url(self, obj):
    #     print(obj.data)
    #     return obj.get_absolute_url()

    class Meta:
        model = Job
        fields = ('url', 'id', 'name', 'job_type', 'interval', 'status',
                  'to_be_executed_at', 'commence_execution_at',
                  'execution_count', 'created_at', 'updated_at')
        depth = 1
