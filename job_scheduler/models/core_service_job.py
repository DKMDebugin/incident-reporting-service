"""A subclass of Job class"""

from api.models import ProxyManager
from .job import Job


class CoreServiceJob(Job):
    """A subclass of Job class"""
    objects = ProxyManager()

    class Meta:
        proxy = True

    def do_job(self):
        # If job successful return true else return false
        print('doing core service job')
        # self.execution_count = self.execution_count + 1
        return True

    def log_details(self):
        print('logging core service job')
