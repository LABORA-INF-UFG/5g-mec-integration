import json
import socket
from urllib import response
import requests

HTTP_URL = "http://"
HTTPS_URL = "https://"
APP_INST_ID = 1
SERVICE = "10.103.26.38:8000"
CONTENT_TYPE = "application/json"


def make_registry(app):
    
    url = SERVICE + '/service-registry/registry'
    headers = {"Content-Type": CONTENT_TYPE}
    url = HTTP_URL + url
    
    data = {"service_name": "mts-api",    
            "service_ip": f"{socket.gethostbyname(socket.gethostname())}", 
            "service_port": "6000",
            "service_endPoint_Post": "/"
            }
    data_json = json.dumps(data)
    response = requests.post(url=url, data=data_json, headers=headers)
    print (response)
    if response:
        print (response.content)

def check_service_ip(service_name):
    url = SERVICE + '/service-registry/registry/{service_name}'
    headers = {"Content-Type": CONTENT_TYPE}
    url = HTTP_URL + url
    print(url)
    response = requests.get(url=url)
    return response.content