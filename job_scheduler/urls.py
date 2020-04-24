from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import job_create, job_list_detail

urlpatterns = [

    path('jobs/', job_list_detail, name='job_list'),
    path('jobs/<int:pk>/', job_list_detail, name='job_detail'),
    path('jobs/create/', job_create, name='job_create'),

]
