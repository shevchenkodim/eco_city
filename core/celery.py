import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/10'),
        run_every_10_minute.s()
    )


@app.task
def run_every_10_minute():
    """ Tasks for run every 10 minute """
    from broker.indicators.processing_service import processing_service
    processing_service.run_for_type("kmda")
