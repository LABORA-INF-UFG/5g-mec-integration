from flask import Flask, Blueprint, request, jsonify
from validate.validate_content import validate_content
from registry.jwt import encodeToken
import sys
from utils.json import pretty_json
# ---- import models Class ----
from models.registry_model import Registry as registry

service_registry = Blueprint('service_registry', '__name__', url_prefix='/service-registry/<data_type>')

@service_registry.route('', methods=['POST'])
def handle_registry_data(data_type):
    try:
        rc = request.get_json()
        result_msg, result = validate_content(rc)
        if result:
            obj_type = getattr(sys.modules[__name__], data_type)
            result = handle_post(obj_type)
            token, encode_status = encodeToken(rc)
            if encode_status == 201:
                response = Flask.response_class(response=token, status=201)
                return response
            else:
                response = "Token generation failed"
                response = Flask.response_class(response=token, status=400)
                return response
        else:
            response = Flask.response_class(response=result_msg, status=406)
            return response
    except Exception as e:
        return e

@service_registry.route('/<service_name>', methods=['GET', 'PUT', 'DELETE'])
def handle_specific_data(data_type, service_name):
    obj_type = getattr(sys.modules[__name__], data_type)
    data = obj_type.objects(service_name=service_name).first()
    if not data: return jsonify({'error': 'data not found'})
    if request.method == 'GET': return handle_get(data)
    elif request.method == 'PUT': return handle_put(data)
    elif request.method == 'DELETE': return handle_delete(data)    


def handle_get(data):
    token = encodeToken
    return {"result": pretty_json(data), "token": token}

def handle_post(obj_type):
    if not request.is_json: return {"error": "The request payload is not in JSON format"}
    new_data = obj_type(**request.get_json())
    new_data.save()
    return {"message": f"data has been created successfully.", "result": pretty_json(new_data)}

def handle_put(data):
    from_json(request.get_json(), created=True)
    data.save()
    return {"message": f"data successfully updated", "result": pretty_json(data)}

def handle_delete(data):
    data.delete()
    return {"message": f"Resource successfully deleted.", "result": "OK."}