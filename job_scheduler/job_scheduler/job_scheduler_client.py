"""Client for the JobScheduler type"""

from .job_scheduler import JobScheduler


class JobSchedulerClient:
    """Client for JobScheduler class"""

    @classmethod
    def perform_operation(cls, job_scheduler: JobScheduler):
        job_scheduler.operation()
