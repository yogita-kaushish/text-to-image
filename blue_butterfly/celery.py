from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blue_butterfly.settings')

app = Celery('blue_butterfly',  broker='redis://localhost:6379/0')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()

