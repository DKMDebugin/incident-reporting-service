"""Contains the job scheduler class and client"""

import threading

from .job import Job
from .scheduler import Scheduler


class JobScheduler:
    """JobScheduler is a facade class for job scheduling"""

    def __init__(self, scheduler: Scheduler, job: Job, interval: int):
        self._scheduler = scheduler
        self._job = job()
        self._interval = interval

    def operation(self):
        t = threading.Thread(target=lambda: self._scheduler(self._interval, self._job.do_job))
        t.daemon = True
        t.start()


def job_scheduling_client(job_scheduler: JobScheduler):
    """Client for JobScheduler class"""
    job_scheduler.operation()
