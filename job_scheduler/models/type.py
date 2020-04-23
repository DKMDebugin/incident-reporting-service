"""Contains the ORM for the Type table"""
from django.db import models


class Type(models.Model):
    """The Type model records different possible type of jobs"""
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
