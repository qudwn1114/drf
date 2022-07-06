from celery import shared_task
from config.celery import app
from celery_progress.backend import ProgressRecorder
import datetime
from time import sleep



@shared_task
def longtime_add(x, y):
    f = open("config/test.txt","a")
    f.write(str(datetime.datetime.now()))
    f.close()
    return x + y

@shared_task(bind=True)
def process(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 5, f'On iteration {i}')
    return 'Done'
