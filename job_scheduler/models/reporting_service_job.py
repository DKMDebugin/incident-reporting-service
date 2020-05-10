"""A subclass of Job class"""
from datetime import datetime, timedelta
import pytz

from django.db import models

from api.models import ProxyManager
from .job import Job


class ReportingServiceJob(Job):
    """
        A subclass of Job class which executes all the others types
        of jobs in the reporting service. It will be the only job scheduled
        but execute all other jobs internally
    """
    objects = ProxyManager()

    class Meta:
        proxy = True

    def do_job(self):
        # If job successful return true else return false
        self.status = 'P'
        self.save()
        jobs = Job.objects.all()
        # print(jobs)
        for job in jobs:
            # print(job)
            curr_time = datetime.now()
            curr_time = curr_time.replace(tzinfo=pytz.UTC)
            if job._type != 'reportingservicejob' and job.to_be_executed_at == curr_time:
                print(job)
                job.status = 'P'
                job.log_details()
                job.save()
                is_done = job.do_job()
                generic_job_operation_sequence(job, is_done)
        generic_job_operation_sequence(self, True)
        return True

    def log_details(self):
        print('logging reporting service job')


def generic_job_operation_sequence(job: Job, is_done: bool):
    if is_done:
        job.execution_count = job.execution_count + 1
        new_increase = job.interval.interval * (job.execution_count + 1)
        job.to_be_executed_at = job.commence_execution_at + timedelta(seconds=new_increase)
        job.save()