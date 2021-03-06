"""Contains the ORM for the Job table"""
from django.db import models

from job_scheduler.models import Interval, Type
from api.utilities import Utilities

STATUS = [
    ('P', 'Processing'),
    ('NP', 'Not Processing')
]


class Job(models.Model):
    """The Job model records unique jobs"""
    name = models.CharField(max_length=100, default='')
    job_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    interval = models.ForeignKey(Interval, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS, default='NP')
    execute_at = models.DateTimeField()
    executed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _type = models.CharField(max_length=70)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Utilities.set_type(self, *args, **kwargs)

    def __str__(self):
        return self.name

    def do_job(self):
        pass

    def log_details(self):
        pass
