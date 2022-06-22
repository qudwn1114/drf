from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta
from django.conf import settings
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config',
             broker='amqp://qudwn1114:byoung14@localhost:5672//',
             backend='rpc://',
             include=['config.task'])

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-60-seconds' : {
        'task' : 'config.task.longtime_add',
        'schedule' : crontab(),
        'args': (16, 16)
    },
}
app.conf.timezone = 'Asia/Seoul'