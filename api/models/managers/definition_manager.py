"""The Manager object for the Definition ORM is extended to support bulk delete"""

from django.db import models
from rest_framework.response import Response


class DefinitionManager(models.Manager):
    """Extend definition Manager"""

    def bulk_delete(self, def_ids=[]):
        if self.filter(id__in=def_ids).count() == len(def_ids):
            self.filter(id__in=def_ids).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
