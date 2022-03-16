
import json
from server.constants import *
from server.data_handler import handle_data

import pika
from pika.exchange_type import ExchangeType
from server.listeningService.listeningService import transformlisteningService

class rabbitMQ_Implementation(transformlisteningService):
    
    def __init__(self,exchange,services,hostName=RMQ_HOST,user=RMQ_USER,password=RMQ_PASSWORD):#,routeName,user,password,portNumber,hostName="localhost",exchange="data"
        
        # keeping the shared variable
        self.available_services = services
        
        creds = pika.PlainCredentials(username=user,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName,credentials=creds,port=RMQ_PORT))#port=portNumber, ,  credentials= self.credentials
        channel = connection.channel()
        print (exchange)
        channel.exchange_declare(exchange,exchange_type=ExchangeType.direct)#durable=True,
        
        for api in QUEUES: # each queue is dynamically declared
            channel.queue_declare(queue=api)
            channel.queue_bind(queue=api,exchange=exchange,routing_key=api)
        for api in QUEUES: # each queue is dynamically started
            channel.basic_consume(queue=api, on_message_callback=self.universal_receiver(api), auto_ack=True)
        
        channel.start_consuming()
        
    def universal_receiver(self,api_name): # it could be done in a simpler way.. It's just something that I alaways wanted to try..
        return lambda ch, method, properties, body : self.receiveData(api_name,ch, method, properties, body) # das ist kûnst..
    
    def receiveData(self,api_name,ch,method,properties,body):
        print(body.decode())
        try:
            print(json.loads(body.decode()))
            handle_data(api_name,json.loads(body.decode()))
        except print(0):
            pass
        
# if __name__=="__main__":
#     listener = rabbitMQ_Implementation(RMQ_LISTEN_EXCHANGE)