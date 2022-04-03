import json
from flask import Flask, request, jsonify
import requests
from multiprocessing import Process, Manager
from server.constants import *
from server.listenerImplementation import rabbitMQ_Implementation

manager = Manager()
# this shared data structure will hold services that would receive potential data
transformations = manager.dict()

# print(RMQ_LISTEN_EXCHANGE)
rabbitmq_listener = rabbitMQ_Implementation(RMQ_LISTEN_EXCHANGE,transformations)
# on the other side, rabbitmq is mainly here to handle the system's internal data
# rabbitmq_listener = Process(target=rabbitMQ_Implementation, args=(RMQ_LISTEN_EXCHANGE,transformations,))
# # then I'll tell you all about it when I see you again..
# rabbitmq_listener.start()


app = Flask(__name__)

# countries = [
#     {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
#     {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
#     {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
# ]

transformations = [
    {"id": 1,"url":"", "name": "Thailand", "path": "", "area": 513120},
    {"id": 2,"url":"", "name": "Australia", "capital": "Canberra", "area": 7617930},
]

help_message = "Sorry, can't help you at this particular moment.."

# def _find_next_country_id():
#     return max(country["id"] for country in countries) + 1

def _find_next_transformation_id():
    return max(transformations["id"] for transformations in transformations) + 1

# @app.get("/countries")
# def get_countries():
#     return jsonify(countries)

# @app.post("/countries")
# def add_country():
#     if request.is_json:
#         country = request.get_json()
#         country["id"] = _find_next_country_id()
#         countries.append(country)
#         return country, 201
#     return {"error": "Request must be JSON"}, 415

@app.post("/submit")
def submit_job():
    # try:
        print(request.get_json())
        demand = json.loads(request.get_json())
        print(demand)
        process_query(demand)
            
        return demand,201
    # "Your job has been successfully submitted, thanks for using our services.", 201
    # except :
    #     return {"error": "Request must be JSON, please put your data in the field 'data' and don't forget the field 'road_map', that uses id's already provided by our_ip_address/transformationScripts"}, 415


@app.get("/")
def get_help_message():
    return help_message

@app.get("/transformationScripts")
def get_transformationScripts():
    return jsonify(transformations)

@app.post("/transformationScripts")
def add_scripts():
    if request.is_json:
        transformationScript = request.get_json()
        transformationScript["id"] = _find_next_transformation_id()
        transformations.append(transformationScript)
        return transformationScript, 201
    return {"error": "Request must be JSON"}, 415

def process_query(demand):
    list = demand["road_map"];
    next_transformation_id = list.pop()
    print(next_transformation_id)
    demand["road_map"] = list
    destination = [x for x in transformations if x["id"] == next_transformation_id].pop()
    print(destination)
    _send_query(destination,demand)

def _send_query(transformation,data):
    # pload = {'road_map':[2,6,1],'data':'123'}
    r = requests.post(transformation.url,json= json.dumps(transformation))
    # print(r.text)