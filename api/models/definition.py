"""Definition ORM layers the table that records the different definitions of report"""

from django.db import models
from django_mysql.models import ListCharField

from .managers import DefinitionManager


class Definition(models.Model):
    """Bug report definition"""
    frequency = models.ForeignKey('Frequency', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    project_uuid = models.CharField(max_length=100, default='')
    template_uuid = models.CharField(max_length=100, default='')  # new field
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
        return f"{self.id}"

    def calculate_next_exec_date(self):
        pass
