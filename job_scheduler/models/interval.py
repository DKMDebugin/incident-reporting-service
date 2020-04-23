"""Contains the ORM for the Interval table"""
from django.db import models


class Interval(models.Model):
    """The Interval model records different possible job intervals"""
    interval = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.interval}'
