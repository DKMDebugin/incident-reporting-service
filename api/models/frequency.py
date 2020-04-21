"""Frequency ORM layers the table that records frequency with which report will be sent."""

from django.db import models


class Frequency(models.Model):
    """stores frequency of sending out reports"""
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
