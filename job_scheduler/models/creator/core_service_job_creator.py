"""
JobCreator is subclass of Creator class.
factory_method will return a Job object
"""
from datetime import datetime

from api.utilities import Utilities

from job_scheduler.models import Job, CoreServiceJob, Type, Interval
from .creator import Creator


class CoreServiceJobCreator(Creator):
    """A concrete class of the Creator class"""

    def __init__(self, name: str, job_type: str, interval: int, execute_at: datetime):
        self.name = name
        self.job_type = job_type
        self.interval = interval
        self.execute_at = execute_at

    def factory_method(self) -> CoreServiceJob:
        """factory_method creates and returns an object of type Job"""

        return CoreServiceJob.objects.create(
            name=self.name, job_type=self.job_type, interval=self.interval,
            execute_at=Utilities.covert_str_to_datetime(self.execute_at)
        )

    def operation(self):
        """Validate job interval and type then create object"""
        job = Job.objects.filter(name=self.name)
        if job:
            return None

        prev_type = Type.objects.filter(name=self.job_type)
        prev_interval = Interval.objects.filter(interval=self.interval)
        if not prev_type:
            self.job_type = Type.objects.create(name=self.job_type)
        else:
            self.job_type = prev_type[0]
        if not prev_interval:
            self.interval = Interval.objects.create(interval=self.interval)
        else:
            self.interval = prev_interval[0]

        return self.factory_method()
