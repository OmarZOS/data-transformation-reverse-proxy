
import requests

def rest_send_data(url,data):
    response = requests.post(url,data)
    return (response.status_code,response.reason,) 

