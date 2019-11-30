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
from django.contrib import admin
from django.urls import path, include
import py_eureka_client.eureka_client as eureka_client
import os
from decouple import config

from api.jobs import (
                Facade,
                JobCoreService,
                job_client,
                Scheduler
                )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]


# Register to eureka server
eureka_client.init(eureka_server=config("EUREKA_SERVER"),
                   app_name="reporting",
                   instance_port=config("EUREKA_SERVER_PORT", cast=int))


# run job
interval = 5
facade = Facade(Scheduler, JobCoreService, interval)
job_client(facade)
