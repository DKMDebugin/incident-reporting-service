"""A subclass of JobScheduler that implements the essential operations for job to be scheduled"""

import threading

from job_scheduler.models.job import Job
from job_scheduler.scheduler import Scheduler
from .job_scheduler import JobScheduler


class JobSchedulerConcrete(JobScheduler):
    """JobSchedulerConcrete class implements operation method """

    def __init__(self, scheduler: Scheduler, job: Job):
        self._scheduler = scheduler
        self.job = job
        self._interval = job.interval.interval

    def do_job(self):
        self.job.do_job()

    def operation(self, do_job) -> None:
        if not do_job:
            t = threading.Thread(target=lambda: self._scheduler(self._interval, self.do_job))
        else:
            t = threading.Thread(target=lambda: self._scheduler(self._interval, do_job))
        t.daemon = True
        t.start()
