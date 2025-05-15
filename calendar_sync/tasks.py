from celery import shared_task
from . import service

@shared_task
def sync_calendar():
    service.incremental_sync() 