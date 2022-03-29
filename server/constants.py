
import os

QUEUES = ['Twitter','Facebook','Youtube']

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
RMQ_PORT = str(os.getenv("RABBIT_MQ_PORT"))    
RMQ_PUBLISH_EXCHANGE = str(os.getenv("RABBIT_MQ_PUBLISH_EXCHANGE"))
RMQ_LISTEN_EXCHANGE = str(os.getenv("RABBIT_MQ_LISTEN_EXCHANGE"))

BROKER_TYPE= "RabbitMQ_TYPE"
REST_TYPE= "REST_TYPE"











