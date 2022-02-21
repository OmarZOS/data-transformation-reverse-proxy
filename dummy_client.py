import json
import requests
pload = {'road_map':[2,6,1],'data':'123'}
r = requests.post('http://localhost:5000/submit',json= json.dumps(pload))
print(r.text)