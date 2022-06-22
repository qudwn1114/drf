from celery import shared_task
import datetime

@shared_task
def longtime_add(x, y):
    f = open("config/test.txt","a")
    f.write(str(datetime.datetime.now()))
    f.close()
    return x + y