from rest_framework import viewsets, permissions
from rest_framework import status, generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Frequency, Type, Definition, Report
from .serializers import (
                           FrequencySerializer, TypeSerializer,
                           DefinitionSerializer, ReportSerializer
                        )
from .permissions import IsReadOnly


class FrequencyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer

class TypeViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class DefinitionViewset(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

    def bulk_destroy(self, request, pk=None):
        if pk is None:
            def_ids= request.query_params.get('def_ids', None)
            Definition.objects.bulk_delete(def_ids=def_ids)
        else:
            instance = self.get_object(pk)
            if not instance:
                return Response(status=status.HTTP_404_NOT_FOUND)
            instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class DefinitionBulkDelete(generics.DestroyAPIView):
#     model = Definition
#     serializer_class = DefinitionSerializer
#     # lookup_field = "id"
#
#     def get_queryset(self):
#         # print(self.request.query_params)
#         params=self.request.query_params.get("def_list", None)
#         print(params)
#         def_list=[]
#         for param in params.split(","):
#             pk.append(int(param))
#         return Definition.objects.bulk_delete(def_list=def_list)
#
# # @csrf_exempt
# def definition_bulk_delete(request):
#     # print(self.request.query_params)
#     if request.method=="DELETE":
#         print(request)
#         # params=request.DELETE.get("def_list", "")
#         # print(params)
#         # def_list=[]
#         # if params is not "":
#         #     for param in params.split(","):
#         #         def_list.append(int(param))
#         #     return Definition.objects.bulk_delete(def_list=def_list)
#     return HttpResponse("200")

class ReportViewset(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
