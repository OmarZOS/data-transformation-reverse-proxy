
import wrappers.RabbitMQ_client as broker_channel
import wrappers.REST_client as rest_channel
from constants import *

def data_publisher(self,func):
        async def wrapper_function(*args, **kwargs):
            if("road_map" in data):
                # keep it pending, while data is transformed
                roadmap = data.pop("road_map")
                destination = roadmap["road_map"].pop(0)
            
            func(*args,  **kwargs)
            if(roadmap):
                data["roadmap"]=roadmap

            if(destination):
                if("type" in destination):
                    if(destination["type"] == REST_TYPE):
                        response = await rest_channel.rest_send_data(destination["url"],data)
                        return response
                
                if("exchange" in destination):
                    broker_channel.send_data(api,data,destination["exchange"])
                    return "Data sent to Broker"
            
            # every road you take.. will always lead you home..
            broker_channel.send_data(api,data)
        return wrapper_function

# this decoration was made to simplify the handling process
@data_publisher
async def handle_data(api,data):
    # transforming
    data = await transform_data(data)
    
async def transform_data(data):
    # default transforming..
    return data
    
    

