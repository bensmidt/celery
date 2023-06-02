from celery import Celery
from rabbitmq import RabbitMQ
from redis import Redis
from time import sleep

server = Celery(
    'tasks', 
    broker='pyamqp://guest:guest@localhost:5672//', 
    backend='redis://localhost:6379/0'
)
server.conf.task_track_started = True

@server.task
def reverse(text: str): 
    sleep(5)
    return text[::-1]
