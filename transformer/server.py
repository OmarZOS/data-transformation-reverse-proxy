from multiprocessing import  Process #,Manager
from listenerImplementation import rabbitMQ_Implementation as Listener
from fastapi import BackgroundTasks,FastAPI
from models import *
from constants import *
import data_handler as d_handler
import query_handler as q_handler

# ----------- App initialisation ---------------------------------------

# manager = Manager()
# # this shared data structure will hold services that would receive potential data
# transformations = manager.dict()

app = FastAPI();

# on the other side, rabbitmq is mainly here to handle the system's internal data
listener = Process(target=Listener, args=(RMQ_LISTEN_EXCHANGE,))
# # then I'll tell you all about it when I see you again..
listener.start()

extractor_services = {}

@app.get("/")
def root():
    return {"message": "Welcome to phoros' transformation services "}

# ----------- Transformation ---------------------------------

@app.get("/transformer/details")
def transformers():
    return {"message": "Es kommt der tag andem du es kennt, doch ist es nicht heute."}

@app.get("/transformer/transform")
async def transformers(query: Query):
    response = await d_handler.handle_data(query.api,query.content)
    return {"message": f"{response}"}
