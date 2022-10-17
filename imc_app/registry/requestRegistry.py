import json
import socket
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
    data = {"service_name": "imc-calc",    
            "service_ip": f"{socket.gethostbyname(socket.gethostname())}",
            "service_port": "5000",
            "service_endPoint_Post": "/imc-calc"
            }
    data_json = json.dumps(data)
    response = requests.post(url=url, data=data_json, headers=headers)

    if response:
        print (response.content)
    
