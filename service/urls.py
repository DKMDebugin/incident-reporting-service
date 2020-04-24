"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import py_eureka_client.eureka_client as eureka_client

from decouple import config

from job_scheduler.job_scheduler import JobSchedulerCreator
from job_scheduler.models import CoreServiceJobCreator
from job_scheduler.scheduler import Scheduler
from job_scheduler.job_scheduler import JobSchedulerClient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include('job_scheduler.urls')),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Register to eureka server
# try:
#     eureka_client.init(eureka_server=config("EUREKA_SERVER"),
#                        app_name="REPORTING",
#                        instance_host="ims-reporting.herokuapp.com",
#                        instance_port=config("EUREKA_SERVER_PORT", cast=int),
#                        # port=eureka_client.PortWrapper(443, true)
#                        )
#
# except Exception as e:
#     # print("* * * *\nUnable to connect to eureka server.\nCheck device internet & server connection.\n* * * *\n")
#     print(e)

# run job
# interval = 5
# job_scheduler = JobScheduler(Scheduler, JobCoreService, interval)
# job_scheduling_client(job_scheduler)

# job = CoreServiceJobCreator('first job', 'daily job', 5, datetime.now()).operation()
# # job_scheduler = JobSchedulerConcrete(Scheduler, job)
# job_scheduler_proxy = JobSchedulerCreator().create_job_scheduler_concrete_proxy(Scheduler, job)
# JobSchedulerClient.perform_operation(job_scheduler_proxy)
