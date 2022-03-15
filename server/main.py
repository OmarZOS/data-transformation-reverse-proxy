# A simple rabbitmq listener..

import json
import pika






creds = pika.PlainCredentials(username="omar",password="omar")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=creds))
channel = connection.channel()

channel.queue_declare(queue='Twitter')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body.decode()))

channel.basic_consume(queue='Twitter', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()