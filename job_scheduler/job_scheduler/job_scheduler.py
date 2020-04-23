"""Contains the job scheduler class and client"""

from abc import ABC, abstractmethod


class JobScheduler(ABC):
    """Base abstract class for all job scheduler"""

    @abstractmethod
    def do_job(self) -> None:
        pass

    @abstractmethod
    def operation(self) -> None:
        pass
