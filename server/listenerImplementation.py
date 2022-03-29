
import json
from constants import *
from data_handler import handle_data

import pika
from pika.exchange_type import ExchangeType
from listeningService.listeningService import listeningService

class rabbitMQ_Implementation(listeningService):
    
    def __init__(self,exchange,hostName=RMQ_HOST,user=RMQ_USER,password=RMQ_PASSWORD):#,routeName,user,password,portNumber,hostName="localhost",exchange="data"
        
        # keeping the shared variable
        # self.available_services = services
        
        print("Listening with: ----------------------")
        print(exchange)
        print(hostName)
        print(user)
        print(password)
        print("---------------------------------------")

        creds = pika.PlainCredentials(username=user,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName,credentials=creds,port=RMQ_PORT))#port=portNumber, ,  credentials= self.credentials
        channel = connection.channel()
        
        channel.exchange_declare(exchange,exchange_type=ExchangeType.direct) # durable=True,
        
        for api in QUEUES: # each queue is dynamically declared
            channel.queue_declare(queue=api)
            channel.queue_bind(queue=api,exchange=exchange,routing_key=api)
        for api in QUEUES: # each queue is dynamically started
            channel.basic_consume(queue=api, on_message_callback=self.universal_receiver(api), auto_ack=True)
        
        channel.start_consuming()
        
    def universal_receiver(self,api_name): # it could be done in a simpler way.. It's just something that I alaways wanted to try..
        return lambda ch, method, properties, body : self.receiveData(api_name,ch, method, properties, body) # das ist kûnst..
    
    def receiveData(self,api_name,ch,method,properties,body):
        # print(body.decode())
        # try:
        # print(json.loads(body.decode()))
        data = json.loads(body.decode())
        if("roadmap" in data):
            data["roadmap"],next_destination = self.resolve_service_ids(data["roadmap"])
    
        # for now, I just hardcoded it..
        next_destination = {"type":"rabbitmq"}
        
        handle_data(api_name,data,next_destination)
        # except :
        # print("An error has occured, please take measures")
            # pass
    def resolve_service_ids(self,roadmap): # takes the roadmap, and gets you access to the next destination
        return roadmap,{}
        
# if __name__=="__main__":
#     listener = rabbitMQ_Implementation(RMQ_LISTEN_EXCHANGE)