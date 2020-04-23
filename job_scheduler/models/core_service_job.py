"""A subclass of Job class"""

from api.models import ProxyManager
from .job import Job


class CoreServiceJob(Job):
    """A subclass of Job class"""
    objects = ProxyManager()

    class Meta:
        proxy = True

    def do_job(self):
        print('doing core service job')

    def log_details(self):
        print('logging core service job')
