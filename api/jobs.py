import threading, time

class Scheduler:
    """Scheduler class for jobs. It autos starts after initialization"""
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
          self.next_call += self.interval
          self._timer = threading.Timer(self.next_call - time.time(), self._run)
          self._timer.start()
          self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class Job:
    """Parent class for all jobs"""
    def do_job(self):
        pass

class JobCoreService(Job):
    """Job for core service"""
    def do_job(self):
        print('doing job')
        # res = eureka_client.do_service("CORESERVICE", "/service/context/path")

class Facade:
    """Facade class for job scheduling"""
    def __init__(self, scheduler: Scheduler, job: Job, interval: int):
        self._scheduler = scheduler
        self._job = job()
        self._interval = interval

    def operation(self):
        t = threading.Thread(target=lambda: self._scheduler(self._interval, self._job.do_job))
        t.daemon = True
        t.start()

def job_client(facade: Facade):
    """Client for Facade class"""
    facade.operation()
