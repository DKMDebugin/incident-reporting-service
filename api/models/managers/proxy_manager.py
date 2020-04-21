"""The Manager object is extended to support 1-1 inheritance"""

from django.db import models


class ProxyManager(models.Manager):
    """ProxyManager"""

    def get_queryset(self):
        return super(ProxyManager, self).get_queryset().filter(_type=self.model.__name__.lower())
