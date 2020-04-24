"""
JobScheduler is subclass of Creator class.
The factory methods will return different children of JobScheduler object.
"""

from .creator import Creator
from job_scheduler.job_scheduler import JobSchedulerConcrete, JobSchedulerConcreteProxy
from job_scheduler.models import Job
from job_scheduler.scheduler import Scheduler


class JobSchedulerCreator(Creator):
    """A concrete class of the Creator class"""

    def create_job_scheduler_concrete(self, scheduler: Scheduler, job: Job) -> JobSchedulerConcrete:
        """returns a concrete job scheduler"""
        return JobSchedulerConcrete(scheduler, job)

    def create_job_scheduler_concrete_proxy(self, scheduler: Scheduler, job: Job) -> JobSchedulerConcreteProxy:
        """returns a concrete job scheduler proxy"""
        return JobSchedulerConcreteProxy(
            self.create_job_scheduler_concrete(scheduler, job)
        )
