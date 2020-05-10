"""Report ORM layers the table that records the kinds of bug report"""

from django.db import models

from api.utilities import Utilities


class Report(models.Model):
    """File attachment for  bug definition"""
    definition = models.ForeignKey("Definition", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    attachment = models.FileField(
        upload_to=Utilities().upload_folder_file_path("bug_report"),
        blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _type = models.CharField(max_length=70)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Utilities.set_type(self, *args, **kwargs)

    def __str__(self):
        return f"{self.id}"

    @property
    def _type(self):
        return self.___type

    @_type.setter
    def _type(self, _type):
        self.___type = _type

    def generate_report(self):
        pass

    def get_bug_info(self):
        pass

    def get_issue_info(self):
        pass
