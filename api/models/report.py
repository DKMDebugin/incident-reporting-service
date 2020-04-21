"""Report ORM layers the table that records the kinds of bug report"""

from django.db import models

from api.utilities import upload_file_path


class Report(models.Model):
    """File attachment for  bug definition"""
    definition = models.ForeignKey("Definition", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    attachment = models.FileField(upload_to=upload_file_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _type = models.CharField(max_length=70)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.__class__.__subclasses__():
            self._type = self.__class__.__name__.lower()
        else:
            subclass = [x for x in self.__class__.__subclasses__() if x.__name__.lower() == self._type]
            if subclass:
                self.__class__ = subclass[0]
            else:
                self._type = self.__class__.__name__.lower()

    def __str__(self):
        return f"{self.id}"

    def generateReport(self):
        pass

    def getBugInfo(self):
        pass

    def getIssueInfo(self):
        pass
