"""A subclass of Report class"""

from .managers import ProxyManager
from .report import Report


class BugCreatedReport(Report):
    """A subclass of Report class"""
    objects = ProxyManager()

    class Meta:
        proxy = True
