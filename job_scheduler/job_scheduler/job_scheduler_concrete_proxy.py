"""A subclass of JobScheduler that implements non-essential operations for the scheduled job such as logging"""

from job_scheduler.models import Log
from .job_scheduler import JobScheduler


class JobSchedulerConcreteProxy(JobScheduler):
    """
    JobSchedulerConcreteProxy class implements operation method by delegating it to the concrete implementation
     of the JobScheduler. It also implement non essential operation such as logging.
     """

    def __init__(self, job_scheduler: JobScheduler):
        self.job_scheduler = job_scheduler

    def do_job(self):
        self.log_job()
        self.job_scheduler.do_job()
        self.log_job()

    def operation(self) -> None:
        self.job_scheduler.operation(self.do_job)

    def log_job(self):
        job = self.job_scheduler.job
        job.log_details()
        # prev_log = Log.objects.filter(job)
        # if not prev_log:
        #     with open('log_file.txt', 'w') as file:
        #         file.write(job.log_details())
        #         Log.objects.create(job, file)
