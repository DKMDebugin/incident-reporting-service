from django.db import models
from django.db.models import Manager
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response

from django_mysql.models import ListCharField

# Create your models here.
class Frequency(models.Model):
    """stores frequency of sending out reports"""
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    """Types of reports"""
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generateReport(self):
        pass

    def getBugInfo(self):
        pass

    def getIssueInfo(self):
        pass

class DefinitionManager(Manager):
    """Extend definition Manager"""
    def bulk_delete(self, def_list=[]):
        no_of_items = len(def_list)
        message = {"Recieved": no_of_items}
        if no_of_items > 0:
            del_tup = self.objects.filter(
                                pk__in=def_list).delete()
            message["Deleted"] = del_tup[0]
            if del_tup[0] == no_of_items:
                return Response(success_message, status=status.HTTP_200_OK)
            return Response(content, status=status.HTTP_409_CONFLICT)
        return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)

class Definition(models.Model):
    """Bug report definition"""
    frequency = models.ForeignKey('Frequency', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    project_uuid = models.CharField(max_length=100, default='')
    roles = ListCharField(
            base_field=models.CharField(max_length=10),
            max_length=(6 * 11),
            default=[]
            )
    users = ListCharField(
            base_field=models.CharField(max_length=10),
            max_length=(6 * 11),
            default=[]
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    next_execution_date = models.DateTimeField(auto_now=True)

    objects = DefinitionManager()


    def __str__(self):
        return self.id

    def calculateNextExecDate(self):
        pass

class Report(models.Model):
    """File attachment for  bug definition"""
    definition = models.ForeignKey("Definition", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    attachment = models.FilePathField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    def generateReport(self):
        pass

    def getBugInfo(self):
        pass

    def getIssueInfo(self):
        pass
