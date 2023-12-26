from multiprocessing import cpu_count

bind = 'unix:/home/crud.uz/gunicorn.sock'

workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

loglevel = 'debug'
accesslog = '/home/crud.uz/access_log'
errorlog = '/home/crud.uz/error_log'
