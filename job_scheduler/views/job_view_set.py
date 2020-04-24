"""Contains the JobViewSet class with handles post and get http request"""

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from job_scheduler.models import Job, CoreServiceJobCreator
from job_scheduler.serializers import JobSerializer


# class JobViewSet(viewsets.ViewSet):
#     """
#     JobViewSet for creating, listing, and retrieving jobs
#     """
#
#     def list(self, request):
#         queryset = Job.objects.all()
#         serializer = JobSerializer(queryset, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Job.objects.all()
#         job = get_object_or_404(queryset, pk=pk)
#         serializer = JobSerializer(job, context={'request': request})
#         return Response(serializer.data)

@api_view(['GET'])
def job_list_detail(request, pk=None):
    if request.method == 'GET':
        queryset = Job.objects.all().values()
        # print(queryset.values())
        if pk:
            job = list(Job.objects.filter(pk=pk).values())[0]
            # print(job)
            serializer = JobSerializer(data=job, context={'request': request})
        else:
            jobs = list(queryset)
            serializer = JobSerializer(data=jobs, context={'request': request}, many=True)
        # print(serializer.errors)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)


@api_view(['POST'])
def job_create(request):
    if request.method == 'POST':
        data = request.data
        created_job = CoreServiceJobCreator(data.get('name'), data.get('job_type'),
                                            data.get('interval'), data.get('execute_at')).operation()
        if created_job is not None:
            content = {'message': 'Job created!'}
            return Response(content, status=status.HTTP_201_CREATED)

        content = {'message': 'A job with the same name already exist!', 'data': data}
        return Response(content, status=status.HTTP_200_OK)
