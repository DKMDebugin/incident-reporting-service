"""
JobCreator is subclass of Creator class.
factory_method will return a Job object
"""
from datetime import datetime, timedelta

from api.utilities import Utilities

from job_scheduler.models import Job, CoreServiceJob, Type, Interval
from .creator import Creator


class CoreServiceJobCreator(Creator):
    """A concrete class of the Creator class"""

    def __init__(self, name: str, job_type: str, interval: int, commence_execution_at: str):
        self.name = name
        self.job_type = job_type
        self.interval = interval
        self.to_be_executed_at = None
        self.commence_execution_at = commence_execution_at

    def factory_method(self) -> CoreServiceJob:
        """factory_method creates and returns an object of type Job"""

        return CoreServiceJob.objects.create(
            name=self.name, job_type=self.job_type, interval=self.interval,
            to_be_executed_at=self.to_be_executed_at,
            commence_execution_at=self.commence_execution_at
        )

    def operation(self):
        """Validate job interval and type then create object"""
        job = CoreServiceJob.objects.filter(name=self.name)
        if job:
            return None

        prev_type = Type.objects.filter(name=self.job_type)
        prev_interval = Interval.objects.filter(interval=self.interval)
        time_array = self.commence_execution_at.split('-')

        if not prev_type:
            self.job_type = Type.objects.create(name=self.job_type)
        else:
            self.job_type = prev_type[0]
        if not prev_interval:
            self.interval = Interval.objects.create(interval=self.interval)
        else:
            self.interval = prev_interval[0]

        if len(time_array) == 3:
            self.commence_execution_at = datetime(time_array[0], time_array[1], time_array[2])
            self.to_be_executed_at = self.commence_execution_at
            # self.to_be_executed_at = self.commence_execution_at + timedelta(seconds=self.interval.interval)

        return self.factory_method()
