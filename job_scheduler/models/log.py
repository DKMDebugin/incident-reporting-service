"""Contains the ORM for the Log table"""
from django.db import models

from job_scheduler.models import Job
from api.utilities import Utilities


class Log(models.Model):
    """The Log model records job activities"""
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=Utilities.upload_folder_file_path('job_log'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
