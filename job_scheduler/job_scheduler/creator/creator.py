"""Creator class is the super class for JobScheduler object creators."""
from abc import ABC, abstractmethod

from job_scheduler.job_scheduler import JobSchedulerConcrete, JobSchedulerConcreteProxy
from job_scheduler.models import Job
from job_scheduler.scheduler import Scheduler


class Creator(ABC):
    """Creator abstract base class defines the factory methods"""

    @abstractmethod
    def create_job_scheduler_concrete(self, scheduler: Scheduler, job: Job) -> JobSchedulerConcrete:
        """returns a concrete job scheduler"""
        pass

    @abstractmethod
    def create_job_scheduler_concrete_proxy(self, scheduler: Scheduler, job: Job) -> JobSchedulerConcreteProxy:
        """returns a concrete job scheduler proxy"""
        pass
