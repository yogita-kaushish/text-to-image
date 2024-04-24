cd ..
celery -A blue_butterfly worker --purge --loglevel=info --pool=solo 
