import json
import os
import pika
from pika.exchange_type import ExchangeType

RMQ_HOST = str(os.getenv("RABBIT_PUBLISH_MQ_HOST"))
RMQ_PORT = str(os.getenv("RABBIT_PUBLISH_MQ_PORT"))
RMQ_USER = str(os.getenv("RABBIT_PUBLISH_MQ_PUBLISH_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PUBLISH_PASSWORD"))
EXCHANGE = str(os.getenv("RABBIT_MQ_PUBLISH_EXCHANGE"))

def rmq_send_data(api,data):
    
    creds = pika.PlainCredentials(username=RMQ_USER,password=RMQ_PASSWORD)
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQ_HOST,credentials=creds))
    channel = connection.channel()

    # # das scheint undeutlisch zu sein..
    channel.queue_declare(queue=api)
    channel.exchange_declare(EXCHANGE,exchange_type=ExchangeType.direct)
    channel.queue_bind(queue=api,exchange=EXCHANGE,routing_key="Twitter")

    channel.basic_publish(exchange=EXCHANGE, routing_key=api, body=json.dumps(data))
    print(" [x] Sent Data!'")
    connection.close()










