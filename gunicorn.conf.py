import os
import gevent.monkey
gevent.monkey.patch_all()

#import multiprocessing

loglevel = 'info'
bind = '0.0.0.0:80'
backlog = 512
pidfile = '/run/gunicorn.pid'
accesslog = '/var/log/gunicorn.log'
errorlog = '/var/log/gunicorn.log'
daemon = True
chdir = '/usr/local/flask'

#workers = multiprocessing.cpu_count() * 2 + 1
workers = 2
threads = 2
max_requests = 2048
worker_class = 'gevent'
worker_connections = 512
timeout = 30
graceful_timeout = 30
keepalive = 2
