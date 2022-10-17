from ast import Try
import json
from flask import Blueprint, request, Flask
import requests
from flask_jwt_extended import jwt_required
from registry.Registry import check_service_ip


dataM = Blueprint('dataManager', 'dataManager', url_prefix='/')
services=["imc-calc"]
data = []


@dataM.route('/', methods=['POST'])
#@jwt_required()
def postData():
    try:
        request_info = request.get_json()
        if request_info["service_ip"] and request_info["method"]:
            service_ip = request_info["service_ip"]
            method = request_info["method"]
            data = request_info["data"]
            response = makeRequest(data, service_ip, method)
            if response.status_code == 201:
                response = Flask.response_class(response=response.content, status=201)
            else:
                response = Flask.response_class(response=response, status=404)
        elif request_info["service_name"]:
            response = check_service_ip(request_info["service_name"])
        else:
            response = Flask.response_class(response="Service IP and Method Requested", status=404)
        return response
    except Exception as e:
        return e, 500
    
def makeRequest (data, ip, method):
    try:
        if method == "POST":
            header = {
            'Content-Type': 'application/json',
            }   
            data_json = json.dumps(data)
            response = requests.post(url=ip, data=data_json, headers=header)
            return response
        if method == "GET":
            response = requests.get(ip)
            return response
        if method == "PUT": 
            data_json = json.dumps(data)
            response = requests.put(ip, data=data)
            return response
        if method == "DELETE":
            response = requests.put(ip)
            return response
    except Exception as e:
        return e, 500