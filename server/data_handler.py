
import wrappers.RabbitMQ_client as broker_channel

def handle_data(api,data,destination):
    
    print("Sending ")
    print(data)
    broker_channel.send_data(api,data)
    
    
    
    # if(data["road_map"]):
        
    # else:
    #     pass
    
    
    # indexer = Indexer(api)
    
    for (k,values) in data.items():
        
        print("received dateien..")
        print(k)
        print(values)
        
        # if isinstance(values,list):
        #     # print(values)
        #     for item in values:
        #         if "id" in item.keys() or "other" in item.keys():
        #             _doc_id = ["other","id"]("id" in item.keys())
        #             indexer.index(doc_type=k,doc_id=str(_doc_id),doc_body=item)
        #     #     pass