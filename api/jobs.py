import threading, time

import py_eureka_client.eureka_client as eureka_client

class Job:
    """Parent class for all jobs"""
    def do_job(self):
        pass

class JobCoreService(Job):
    """Job for core service"""
    def do_job(self):
        print('doing job')
        # response = eureka_client.do_service_async("CORESERVICE", "/service/context/path",
        #                             on_success= success_callback, on_error=error_callback)


def success_callback(data):
    print(data)

def error_callback(error):
    print(error)
