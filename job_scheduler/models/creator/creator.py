"""Creator class is the super class for all creators."""
from abc import ABC, abstractmethod

from job_scheduler.models import Job


class Creator(ABC):
    """Creator abstract base class defines the factory method"""

    @abstractmethod
    def factory_method(self) -> Job:
        """factory_method returns an object of type Job"""
        pass
