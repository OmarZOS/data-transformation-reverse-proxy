import json
import os
import pika
from pika.exchange_type import ExchangeType

RMQ_HOST = str(os.getenv("RABBIT_MQ_PUBLISH_HOST"))
RMQ_PORT = str(os.getenv("RABBIT_MQ_PUBLISH_PORT"))
RMQ_USER = str(os.getenv("RABBIT_MQ_PUBLISH_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PUBLISH_PASSWORD"))
EXCHANGE = str(os.getenv("RABBIT_MQ_PUBLISH_EXCHANGE"))

# wenn gibt es kein aus weg, ein zufâlliger 
# dateien geht zuruck ins das dateienspeicher..
def send_data(api,data,exchange=EXCHANGE):
    
    creds = pika.PlainCredentials(username=RMQ_USER,password=RMQ_PASSWORD)
    
    print("********************")
    print("Sending via: ")
    print(RMQ_HOST)
    print(RMQ_PORT)
    print(RMQ_USER)
    print(RMQ_PASSWORD)
    print(exchange)
    print("********************")

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQ_HOST,credentials=creds))
    channel = connection.channel()
    # # das mir scheint undeutlisch zu sein..
    channel.queue_declare(queue=api)
    channel.exchange_declare(exchange,exchange_type=ExchangeType.direct)
    channel.queue_bind(queue=api,exchange=exchange,routing_key=api)

    channel.basic_publish(exchange=exchange, routing_key=api, body=json.dumps(data))
    print(" [x] Sent Data!'")
    connection.close()










